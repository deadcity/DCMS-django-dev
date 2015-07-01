###
    @file  backbone-relations.coffee
    @brief Base model class and related classes and functions for providing
        unobtrusive (with respect to the attributes) relations in Backbone
        models.
###


BackboneRelations = Tools.create_namespace 'BackboneRelations'


class BackboneRelations.Model extends Backbone.Model
    ###
        Class function that can be used as a factory to construct the collection
        representing this model's store.

        @NOTE If you decide to override this, it is important to note that the
            store's accessor function identifies the proper collection by
            checking the collection's "model" attribute. If you override
            `_store_factory` and don't want this behavior, you need to override
            the `store` class function as well.
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

        return @_relations =
            '_self' : @
            'one'   : {}
            'many'  : {}

    ###
        Class function to add a -to-one relation to a model.

        @arg name Name of the property on this model to store the instance of
            the referenced model.
        @arg options Configuration for relation.
            @option Model (required) Class for the referenced model. This can
                either be the constructor itself or a string specifying the full
                path to the constructor from the global scope.
            @option attribute (optional; default "<name>_id") The attribute on
                this model that stores the value of the id for the model to be
                referenced.
            @option store (optional; default "_<name>") The name of the member
                variable on this model where a cached copy of the referenced
                model will be stored.

        @event "update-relation:[name]" (this, model, relation_options)
            This event is called whenever the related model is recached. This
            event is triggered just before the referenced model is saved in the
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
                # not yet been set or the related model has not yet been
                # persisted on the server. In case of the latter, assume the
                # store is correctly set.
                return model if attribute is undefined

                # `attribute` being `null` means the relation is set to null.
                if attribute is null
                    if model isnt null
                        @trigger 'update-relation:' + name, @, null, options
                    return @[options.store] = null

                # If cached value is up-to-date, return it.
                if model?.id is attribute
                    return model

                # Fetch (or create) the model.
                if _.isString options.Model
                    options.Model = Tools.resolve options.Model
                model = new options.Model 'id': attribute
                @trigger 'update-relation:' + name, @, model, options

                return @[options.store] = model

            set: (model) ->
                @set options.attribute, model.id
                @trigger 'update-relation:' + name, @, model, options
                @[options.store] = model

    ###
        Class function to add a -to-many relation to a model.

        @arg name Name of the property on this model to store the collection of
            models that reference this one.
        @arg options Configuration for relation.
            @option Model (required unless alternate Collection class is
                specified) Class for the related model. This can either be the
                constructor itself or a string specifying the full path to the
                constructor from the global scope.
            @option attribute (required unless alternate Collection class is
                specified) The attribute on the other model that stores the
                value of this model's id.
            @option store (optional; default "_<name>") The name of the member
                variable on this model where the collection will be stored.
            @option Collection (optional) A constructor for the collection of
                related models. This constructor is responsible for setting up
                anyting needed to keep the collection instance up to date. The
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
                options = _.defaults {}, options,
                    base_collection: options.model.store()

                filter = ->
                    id_value = options.referenced_model.get 'id'
                    attribute = options.referencing_attribute
                    return (model) -> (model.get attribute) is id_value

                options.filter = filter()
                collection = new Tools.Collections.Filtered null, options
                collection.listenTo options.referenced_model, 'change:id', ->
                    collection.set_filter filter()

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
        Class function to initialize polymorphic model inheritance.

        @arg attribute Discriminating attribute on this model which identifies
            which inheritied model a particular instance should be.
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

    ###
        Class function to specify which value maps to this class in a
        polymorphic model inheritance scheme.

        @arg value The value for the discriminating attribute to indicate that
            the model should be an instance of this class.
    ###
    @polymorphic_identity: (value) ->
        @_polymorphic_identity[value] = @

    constructor: (attributes, options) ->
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

        # Normal construction if model does not yet exist.
        super attrs, options
        @constructor.store().add @

        # Anytime the discriminator attribute updates [assuming this model
        # defines one], update the class of this instance.
        if @constructor._polymorphic_on?
            @on 'change:' + @constructor._polymorphic_on, @_update_polymorphic_identity, @

        # When a model is destroyed, remove all references so it can be cleaned
        # up. This should not prevent any already queued event-handlers from
        # being called.
        @on 'destroy', =>
            @stopListening()
            @off()

        return @

    _update_polymorphic_identity: (model, value, options) ->
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
