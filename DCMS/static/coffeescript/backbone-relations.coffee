###
    @file  backbone-relations.coffee
    @brief Base model class and related classes and functions for providing
        unobtrusive (with respect to the attributes) relations in Backbone
        models.

    @dependencies
        underscore-1.8.3.js
        backbone-1.1.2.js
        tools.coffee
        collections.coffee


    There are three primary features of this little library, a common store for
    each model class, "relations" and "polymorphic-models".


    STORE

        Each model class has has a collection that contains every instance of
        that model. We will refer to this collection as the model's "store" and
        it can be accessed through the class-function by that name. If you try
        to create a new instance of a model, the constructor will first check
        that model class's store for an already existing model with the same id.
        If it finds one, it will halt the creation of a new object and return
        the one it found instead. This way, there should only be a single copy
        of any given instance of a model at one time.

        In order to enforce this, it is important that you never change the id
        value of a model instance yourself. You can specify the id when calling
        the model's constructor or you can create a new instance and sync it
        with the server, which will assign the id.


    RELATIONS

        relating-model: The Model class that defines the relationship.

        related-model: The Model class on the other side of the relation.

        referencing-model: The Model class that contains an attribute that
            stores the value of the `id` of the referenced-model. In a -to-one
            relation, this is the relating-model.

        referenced-model: The Model class being related to. In a -to-many
            relation, this is the relating-model.

        There are two class-functions you can call to create new relations on
        the model you are defining, `has_one` and `has_many`. They are called in
        the body of the Model as you are defining it and they each create a
        property (ultimately through `Object.defineProperty`) on the model
        class's prototype. This property stores either an instance of the
        related-model (in the case of `has_one`) or a collection of the related-
        models (in the case of `has_many`).

        Their full use is documented below.


    POLYMORPHIC-MODELS

        The usage pattern for polymorphic-models is based on "Joined Table
        Inheritance" as implemented in SQLAlchemy. It isn't required, but you
        can read up on the pattern in SQLAlchemy's documentation here
        (http://docs.sqlalchemy.org/en/latest/orm/inheritance.html) before
        continuing. You do not have to use Joined Table Inheritance on the
        server-side; polymorphic-models should work just fine with Single Table
        Inheritance as well.

        The notion of a polymorphic-model involves a group of model classes that
        are related in an inheritance hierarchy. There is generally an attribute
        from the base model that indicates which actual model class a particular
        instance is supposed to be. This level of indirection is useful when you
        have semi-generic relations that are loaded asynchronously from the
        server. One model could be configured to reference any model in the
        Model class family by targeting the base model class of that family.
        When the referenced model is instantiated (but the data not yet loaded
        from the server), it will be an instance of the base model. When the
        data is actually loaded, it will automatically update to be an instance
        of the more specific model. Consider the example set of models below.

            class Trait extends BaseModel
                @polymorphic_on 'trait_type'

                defaults: ->
                    id         : undefined
                    trait_type : undefined

            class Affiliation extends Trait
                @polymorphic_identity 'affiliation'

            class Merit extends Trait
                @polymorphic_identity 'merit'

                defaults: ->
                    _.extend super,
                        rating : 1

            class AccessRuleHasTrait extends BaseModel
                defaults: ->
                    id       : undefined
                    trait_id : undefined

                @has_one 'trait', Model: Trait

            has_trait_rule = new AccessRuleHasTrait
                id       : 1
                trait_id : 3

            trait = has_trait_rule.trait

        If an instance of AccessRuleHasTrait is loaded from the server before
        the trait that it references is loaded, an instance for that referenced
        trait will still be created and can be passed around as normal even
        though we don't yet know whether it should be an instance of Affiliation
        or and instance of Merit. When the trait data is eventually loaded from
        the server, the instance itself will update to the appropriate model
        class.
###


BackboneRelations = Tools.create_namespace 'BackboneRelations'


class BackboneRelations.Model extends Backbone.Model
    ###
        Class-function that can be used as a factory to construct the collection
        representing this model's store.

        @NOTE If you decide to override this, it is important to note that the
            store's accessor function identifies the proper collection [in cases
            of inheritance] by checking the collection's "model" attribute. If
            you override `_store_factory` and don't want this behavior, you need
            to override the `store` class-function as well.
    ###
    @_store_factory: ->
        return new Backbone.Collection null, model: @

    ###
        Class function that returns a collection of all instances of this model.
    ###
    @store: ->
        if @_store?.model is @
            return @_store

        return @_store = @_store_factory()

    ###
        Accessor function for meta-information about all of this model's
        relations.
    ###
    @relations: ->
        if @_relations?._self is @
            return @_relations

        # Inherit relations from parent.
        if @_relations?
            relations =
                '_self' : @
                'one'   : _.clone @_relations.one
                'many'  : _.clone @_relations.many
            return @_relations = relations

        # No relations from parent to inherit. Return an empty relations object.
        return @_relations =
            '_self' : @
            'one'   : {}
            'many'  : {}

    ###
        Class-function to add a -to-one relation to a model.

        @arg name Name of the property on this model to store the instance of
            the related-model.
        @arg options Configuration for relation.
            @option Model (required) Class for the related-model. This can
                either be the constructor itself or a string specifying the full
                path to the constructor from the global scope.
            @option attribute (optional; default "<name>_id") The attribute on
                this model that stores the value of the id for the related-
                model.
            @option store (optional; default "_<name>") The name of the member
                variable on this model where a cached copy of the related-
                model will be stored.

        @event "update-relation:[name]" (this, model, relation_options)
            This event is called whenever the related-model is recached. This
            event is triggered just before the related-model is saved to the
            store.

        Relations are property definitions on the prototype, hence they are
        inherited by child classes.
    ###
    @has_one: (name, options) ->
        # Set defaults.
        options = _.defaults {}, options,
            'attribute' : name + '_id'
            'store'     : '_' + name

        # Register relation.
        @relations().one[name] = options

        # Define lazy property.
        @property name,
            get: ->
                attribute = @get options.attribute
                model = @[options.store]

                # `attribute` being `undefined` means either the relation has
                # not yet been set or the referenced-model has not yet been
                # persisted on the server. To accomodate the case of the latter,
                # assume the store is correctly set.
                return model if attribute is undefined

                # `attribute` being `null` means the relation is set to null.
                if attribute is null
                    if model isnt null
                        @trigger "update-relation:#{name}", @, null, options
                    return @[options.store] = null

                # If cached value is up-to-date, return it.
                if model?.id is attribute
                    return model

                # Fetch (or create) the referenced-model.
                # NOTE: This does not fetch the model data from the server.
                if _.isString options.Model
                    options.Model = Tools.resolve options.Model
                model = new options.Model 'id': attribute
                @trigger 'update-relation:' + name, @, model, options

                return @[options.store] = model

            set: (model) ->
                @set options.attribute, model?.id
                @trigger 'update-relation:' + name, @, model, options
                @[options.store] = model

    ###
        Class-function to add a -to-many relation to a model.

        @arg name Name of the property on this model to store the collection of
            related-models.
        @arg options Configuration for relation.
            @option Model (required unless alternate Collection class is
                specified) Class for the related-model. This can either be the
                constructor itself or a string specifying the full path to the
                constructor from the global scope.
            @option attribute (required unless alternate Collection class is
                specified) The attribute on the other model that stores the
                value of this model's id.
            @option store (optional; default "_<name>") The name of the member
                variable on this model where the collection will be stored.
            @option Collection (optional) A constructor for the collection of
                related-models. This constructor is responsible for setting up
                anything needed to keep the collection instance up to date. The
                default value just constructs an instance of
                `Tools.Collections.Filtered` with `Model.store()` as the base
                collection and filtering for models with `attribute` equal to
                this model's id.

        @event "update-relation:[name]" (this, collection, relation_options)
            This event is called whenever the collection of related models is
            recreated. This event is triggered just before the referenced model
            is saved in the store.

        Relations are property definitions on the prototype, hence they are
        inherited by child classes.
    ###
    @has_many: (name, options) ->
        # Set defaults.
        options = _.defaults {}, options,
            'store'      : '_' + name
            'Collection' : (models, options) ->
                generate_filter = ->
                    id_value = options.referenced_model.get 'id'
                    attribute = options.referencing_attribute
                    return (model) -> (model.get attribute) is id_value

                # Set defaults.
                options = _.defaults {}, options,
                    'base_collection' : options.model.store()
                    'filter'          : generate_filter()

                collection = new Tools.Collections.Filtered null, options
                collection.listenTo options.referenced_model, 'change:id', ->
                    collection.set_filter generate_filter()

                return collection

        # Register relation.
        @relations().many[name] = options

        # Define lazy property.
        @property name,
            get: ->
                collection = @[options.store]

                # Collection already initialized.
                return collection if collection?

                # First time accessed.
                if _.isString options.Model
                    options.Model = Tools.resolve options.Model
                collection = new options.Collection null,
                    model                 : options.Model
                    referenced_model      : @
                    referencing_attribute : options.attribute
                @trigger 'update-relation:' + name, @, collection, options

                return @[options.store] = collection

    ###
        Class-function to initialize polymorphic model inheritance.

        @arg attribute Discriminating attribute on this model which identifies
            which inherited model a particular instance should be.
        @arg options Configuration for polymorphic inheritance.
            @option store_factory (optional) A factory to use as the
                _store_factory class function for child models.
                "_polymorphic_on" will instantiate this model's store and then
                set _store_factory to the new factory function so that any child
                classes will use the factory function specified here.
    ###
    @polymorphic_on: (attribute, options) ->
        base_collection = @store()

        # Set defaults.
        options = _.defaults {}, options,
            'store_factory' : (models, options) ->
                options = _.defaults {}, options,
                    model           : @
                    base_collection : base_collection

                polymorphic_identity = _.chain @_polymorphic_identity
                    .pairs()
                    .find (pair) =>
                        [value, Model] = pair
                        return Model is @
                    .value()

                if polymorphic_identity?
                    polymorphic_identity = polymorphic_identity[0]
                    options.filter = (model) ->
                        return (model.get attribute) is polymorphic_identity

                return new Tools.Collections.Filtered null, options

        @_polymorphic_on = attribute
        @_polymorphic_identity = {}
        @_store_factory = options.store_factory
        @_polymorphic_identity_values = {}

    ###
        Class-function to specify which value maps to this class in a
        polymorphic model inheritance scheme.

        @arg value The value for the discriminating attribute to indicate that
            the model should be an instance of this class.
    ###
    @polymorphic_identity: (value) ->
        @_polymorphic_identity[value] = @
        @_polymorphic_identity_values[@name] = value

    constructor: (attributes, options) ->
        polymorphic_on = this.constructor._polymorphic_on
        attrs = attributes || {}
        options || (options = {})

        if options.parse
            attrs = @parse attrs, options
            options = _.clone options
            delete options.parse

        id = attrs[@idAttribute]

        # If model already exists, return it after updating its attributes.
        model = @constructor.store().get id
        if model?
            model.set attrs, options
            return model

        # If model requires but does not specify a polymorphic-identity,
        # automatically apply it here.
        if polymorphic_on? and not attrs[polymorphic_on]?
            pid_values = this.constructor._polymorphic_identity_values
            attrs[polymorphic_on] = pid_values[this.constructor.name]

        # Normal construction if model does not yet exist.
        super attrs, options
        @constructor.store().add @

        # Anytime the discriminator attribute updates [assuming this model
        # defines one], update the class of this instance.
        if @constructor._polymorphic_on?
            @on 'change:' + @constructor._polymorphic_on, @__update_polymorphic_identity, @

        # When a model is destroyed, remove all references so it can be cleaned
        # up. The use of `setTimeout` will allow any already queued event-
        # handlers to finish being called.
        @on 'destroy', =>
            setTimeout =>
                @stopListening()
                @off()
            , 1

        return @

    ###
        Internal method to update the class of the model instance.

        An internal method that gets called in polymorphic-inheritance whenever
        the discriminator attribute changes. This method is responsible for
        changing the class of `this` by manually updating the "__proto__"
        property of the model instance. This is not well tested across different
        browsers but at least works in Chrome.
    ###
    __update_polymorphic_identity: (model, value, options) ->
        old_relations = model.constructor.relations()
        target_model = model.constructor._polymorphic_identity[value]
        model.__proto__ = target_model.prototype
        new_relations = model.constructor.relations()

        # Remove store-attributes for old singular relations that are no longer
        # part of this model.
        for relation in _.difference (_.values old_relations.one), (_.values new_relations.one)
            if model.hasOwnProperty relation.store
                delete model[relation.store]

        # Remove store-attributes for old multi-relations that are no longer
        # part of this model.
        for relation in _.difference (_.values old_relations.many), (_.values new_relations.many)
            if model.hasOwnProperty relation.store
                model[relation.store].off()
                model[relation.store].stopListening()
                delete model[relation.store]

        model.trigger 'update-polymorphic-identity', model, value, options
