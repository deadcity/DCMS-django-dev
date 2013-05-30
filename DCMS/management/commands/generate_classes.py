from os import path
from sys import stdout

from datetime import datetime
from re import sub
from string import Template

from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.db import models

from traits import models as trait_models
from character import models as character_models


def to_unserscores(name):
    s = sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()


class Command (NoArgsCommand):
    def handle_noargs (self, **options):
        trait_types = []
        traits = []

        for attr in dir(trait_models):
            if attr is 'Enum' or attr is 'Trait':
                continue

            Model = getattr(trait_models, attr)
            if not isinstance(Model, type):
                continue

            if issubclass(Model, trait_models.Enum):
                trait_types.append(Model)
            elif issubclass(Model, trait_models.Trait):
                traits.append(Model)

        self.__gen_serializers       ('traits', trait_types + traits, 'trait_serializers')
        self.__gen_views_list_detail ('traits', trait_types + traits, 'traits_ajax')
        self.__gen_urls              ('traits', trait_types + traits, 'traits_ajax')
        self.__gen_backbone_models   ('traits', traits)

        self.__gen_admin_classes ('traits', trait_types, 'enum_admins',  self.__admin_template__enum_admin)
        self.__gen_admin_classes ('traits', traits,      'trait_admins', self.__admin_template__model_admin)


        character_traits = []

        for attr in dir(character_models):
            if attr is 'Character' or attr is 'CharacterHasTrait':
                continue

            Model = getattr(character_models, attr)
            if not isinstance(Model, type):
                continue

            if issubclass(Model, character_models.CharacterHasTrait):
                character_traits.append(Model)

        self.__gen_serializers       ('character', character_traits, 'character_trait_serializers')
        self.__gen_views_list_detail ('character', character_traits, 'character_traits_ajax')
        self.__gen_urls              ('character', character_traits, 'character_traits_ajax')
        self.__gen_backbone_models   ('character', character_traits)

        Character = [character_models.Character]
        self.__gen_serializers       ('character', Character, 'character_serializers')
        self.__gen_views_list_detail ('character', Character, 'character_ajax')
        self.__gen_urls              ('character', Character, 'character_ajax')

        self.__gen_admin_classes ('character', character_traits, 'character_trait_admins',  self.__admin_template__model_admin)
        self.__gen_admin_classes ('character', character_traits, 'character_traits_inline', self.__admin_template__inline_admin)


    # # # # # # # # # #
    # STANDARD HEADER #
    # # # # # # # # # #

    __standard_header = """\
# DCMS auto-generated file
# {}

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


""".format(datetime.now())

    __js_header = """\
// DCMS auto-generated file
// {}

/* * * * * * * * * * * * * * * * * * * * * * *
 * DO NOT MODIFY THE CONTENTS OF THIS FILE!  *
 * * * * * * * * * * * * * * * * * * * * * * */

// If you wish to alter it's contents modify either the source model, or the
// generating tool and then run `manage.py generate_classes` again.  (Don't
// forget to commit the newly generated files!)


""".format(datetime.now())


    # # # # #
    # ADMIN #
    # # # # #

    __admin_template__header = Template("""\
from django.contrib import admin

from ${MODULE_NAME} import ${MODEL_LIST}

""")
    __admin_template__enum_admin = Template("""
class ${MODEL_NAME}Admin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(${MODEL_NAME}, ${MODEL_NAME}Admin)
""")
    __admin_template__model_admin = Template("""
class ${MODEL_NAME}Admin (admin.ModelAdmin):
    list_display = (${LIST_DISPLAY_FIELDS},)
    list_filter  = (${LIST_FILTER_FIELDS},)
admin.site.register(${MODEL_NAME}, ${MODEL_NAME}Admin)
""")
    __admin_template__inline_admin = Template("""
class ${MODEL_NAME}Inline (admin.TabularInline):
    model = ${MODEL_NAME}
""")

    def __gen_admin_classes (self, project, model_list, file_name, template):
        print 'generating enum admin classes for {project}/{file_name}... '.format(project = project, file_name = file_name),
        stdout.flush()

        with open(path.join(settings.PROJECT_PATH, project, 'admin', file_name + '.py'), 'w') as out:
            out.write(self.__standard_header);
            out.write(self.__admin_template__header.substitute(
                MODULE_NAME = model_list[0].__module__,
                MODEL_LIST = ', '.join([Model.__name__ for Model in model_list])
            ))

            for Model in model_list:
                fields = ["'" + field_name + "'" for field_name, field in Model.fields.items()]
                out.write(template.substitute(
                    MODEL_NAME = Model.__name__,
                    LIST_DISPLAY_FIELDS = ', '.join(fields),
                    LIST_FILTER_FIELDS  = ', '.join([field_name for field_name in fields if field_name != "'name'"])
                ))

        print 'done'
        stdout.flush()


    # # # # # # # # # #
    # BACKBONE MODELS #
    # # # # # # # # # #

    __backbone_model_template__main = Template("""\
Models_NS = Tools.create_namespace '${PROJECT}.Models'

class Models_NS.${MODEL_NAME} extends Backbone.Model
    defaults:
        id: null
${FIELD_LIST__DEFAULT}

    parse: (raw) ->
        {
            id: parseInt raw.id, 10
${FIELD_LIST__PARSE}
        }

    toJSON: () ->
        attr = _.clone this.attributes
${FIELD_LIST__JSON}
        attr

    toHumanJSON: () ->
        attr = _.clone this.attributes
${FIELD_LIST__HUMAN_JSON}
        attr

    url: () ->
        "/api/${PROJECT_LOWERCASE}/${MODEL_NAME}/#{ if @id? then "#{@id}/" else '' }"
""")

    __backbone_model_template__default = Template("        ${FIELD_NAME}: null")

    __backbone_model_template__parse_integer = Template("            ${FIELD_NAME}: parseInt raw.${FIELD_NAME}, 10")
    __backbone_model_template__parse_text    = Template("            ${FIELD_NAME}: raw.${FIELD_NAME},")
    __backbone_model_template__parse_enum    = Template("            ${FIELD_NAME}: ${RELATED_PROJECT}.${RELATED_MODEL}.get parseInt raw.${FIELD_NAME}, 10")
    __backbone_model_template__parse_foreign = Template("            ${FIELD_NAME}: ${RELATED_PROJECT}.Objects.${RELATED_MODEL}.get parseInt raw.${FIELD_NAME}, 10")

    __backbone_model_template__json_foreign = Template("        attr.${FIELD_NAME} = attr.${FIELD_NAME}.id")

    __backbone_model_template__human_json_foreign = Template("        attr.${FIELD_NAME} = attr.${FIELD_NAME}.toHumanJSON()")

    def __gen_backbone_models (self, project, model_list):
        print 'generating backbone models for {project}... '.format(project = project),
        stdout.flush()

        target_dir = path.join(settings.PROJECT_PATH, project, 'static', project, 'coffeescript', 'models')
        for Model in model_list:
            with open(path.join(target_dir, Model.__name__.lower() + '.coffee'), 'w') as out:
                out.write(self.__standard_header);

                field_list__default = []
                field_list__parse = []
                field_list__json = []
                field_list__human_json = []

                for field_name, field in Model.fields.items():
                    field_list__default.append(self.__backbone_model_template__default.substitute(FIELD_NAME = field_name))
                    if field_name == 'character':
                        field_list__parse.append(self.__backbone_model_template__parse_integer.substitute(FIELD_NAME = field_name))
                    elif isinstance(field, models.IntegerField):
                        field_list__parse.append(self.__backbone_model_template__parse_integer.substitute(FIELD_NAME = field_name))
                    elif isinstance(field, models.CharField) or isinstance(field, models.TextField):
                        field_list__parse.append(self.__backbone_model_template__parse_text.substitute(FIELD_NAME = field_name))
                    elif isinstance(field, trait_models.EnumField):
                        field_list__parse.append(self.__backbone_model_template__parse_enum.substitute(
                            FIELD_NAME      = field_name,
                            RELATED_PROJECT = field.related.parent_model.__module__.split('.')[0].title(),
                            RELATED_MODEL   = field.related.parent_model.__name__
                        ))
                    elif isinstance(field, models.ForeignKey):
                        field_list__parse.append(self.__backbone_model_template__parse_foreign.substitute(
                            FIELD_NAME      = field_name,
                            RELATED_PROJECT = field.related.parent_model.__module__.split('.')[0].title(),
                            RELATED_MODEL   = field.related.parent_model.__name__
                        ))
                        field_list__json.append(self.__backbone_model_template__json_foreign.substitute(FIELD_NAME = field_name))
                        field_list__human_json.append(self.__backbone_model_template__human_json_foreign.substitute(FIELD_NAME = field_name))
                    else:
                        field_list__parse.append(self.__backbone_model_template__parse_text.substitute(FIELD_NAME = field_name))

                out.write(self.__backbone_model_template__main.substitute(
                    PROJECT    = project.title(),
                    MODEL_NAME = Model.__name__,
                    PROJECT_LOWERCASE    = project,

                    FIELD_LIST__DEFAULT = '\n'.join(field_list__default),
                    FIELD_LIST__PARSE   = '\n'.join(field_list__parse),
                    FIELD_LIST__JSON    = '\n'.join(field_list__json),
                    FIELD_LIST__HUMAN_JSON = '\n'.join(field_list__human_json)
                ))

        print 'done'
        stdout.flush()


    # # # # # # # #
    # SERIALIZERS #
    # # # # # # # #

    __serializer_template__header = Template("""\
from rest_framework import serializers

from ${PROJECT}.models import ${MODEL_NAMES}
""")
    __serializer_template__serializer = Template("""

class ${MODEL_NAME}Serializer (serializers.ModelSerializer):
    class Meta (object):
        model = ${MODEL_NAME}
${MODEL_NAME}.Serializer = ${MODEL_NAME}Serializer
""")

    def __gen_serializers (self, project, model_list, file_name):
        print 'generating serializers for {project}... '.format(project = project),
        stdout.flush()

        with open(path.join(settings.PROJECT_PATH, project, 'serializers', file_name + '.py'), 'w') as out:
            out.write(self.__standard_header);
            out.write(self.__serializer_template__header.substitute(
                PROJECT     = project,
                MODEL_NAMES = ', '.join([Model.__name__ for Model in model_list])
            ))
            for Model in model_list:
                out.write(self.__serializer_template__serializer.substitute(
                    MODEL_NAME = Model.__name__
                ))

        print 'done'
        stdout.flush()


    # # # # #
    # URLS  #
    # # # # #

    __url_template__header = Template("""\
from django.conf.urls import url

from ${PROJECT}.views import ${DETAIL_VIEWS}
from ${PROJECT}.views import ${LIST_VIEWS}

urls = [""")
    __url_template__urls = Template("""
  url(r'^${MODEL_NAME}/(?P<pk>[0-9]+)/$$', ${MODEL_NAME}Detail.as_view()),
  url(r'^${MODEL_NAME}/$$',                ${MODEL_NAME}List.as_view()),
""")
    __url_template__footer = Template("]\n")

    def __gen_urls (self, project, model_list, file_name):
        print 'generating urls for {project}... '.format(project = project),
        with open(path.join(settings.PROJECT_PATH, project, 'urls', file_name + '.py'), 'w') as out:
            out.write(self.__standard_header);
            out.write(self.__url_template__header.substitute(
                PROJECT      = project,
                DETAIL_VIEWS = ', '.join([Model.__name__ + 'Detail' for Model in model_list]),
                LIST_VIEWS   = ', '.join([Model.__name__ + 'List'   for Model in model_list])
            ))
            for Model in model_list:
                out.write(self.__url_template__urls.substitute(
                    MODEL_NAME = Model.__name__
                ))
            out.write(self.__url_template__footer.substitute())

        print 'done'
        stdout.flush()


    # # # # # # # # # # # # #
    # VIEWS : LIST / DETAIL #
    # # # # # # # # # # # # #

    __list_detail_view_template__header = Template("""\
from rest_framework import generics

from ${PROJECT}.models import ${MODEL_NAMES}
from ${PROJECT}.serializers import ${SERIALIZER_NAMES}
""")

    __list_detail_view_template__views = Template("""

class ${MODEL_NAME}Detail (generics.RetrieveUpdateDestroyAPIView):
    model            = ${MODEL_NAME}
    serializer_class = ${MODEL_NAME}Serializer

class ${MODEL_NAME}List (generics.ListCreateAPIView):
    model            = ${MODEL_NAME}
    serializer_class = ${MODEL_NAME}Serializer
""")

    def __gen_views_list_detail (self, project, model_list, file_name):
        print 'generating views (list/detail) for {project}... '.format(project = project),
        stdout.flush()

        with open(path.join(settings.PROJECT_PATH, project, 'views', file_name + '.py'), 'w') as out:
            out.write(self.__standard_header);
            out.write(self.__list_detail_view_template__header.substitute(
                PROJECT          = project,
                MODEL_NAMES      = ', '.join([Model.__name__                for Model in model_list]),
                SERIALIZER_NAMES = ', '.join([Model.__name__ + 'Serializer' for Model in model_list])
            ))
            for Model in model_list:
                out.write(self.__list_detail_view_template__views.substitute(
                    MODEL_NAME = Model.__name__
                ))

        print 'done'
        stdout.flush()
