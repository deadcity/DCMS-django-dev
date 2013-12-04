from os import path

from datetime import datetime
from hashlib import md5
from re import sub

from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.template.loader import render_to_string

from character import models as character_models
from chronicle import models as chronicle_models
from traits import models as trait_models


def to_underscores(name):
    s = sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()


class Command (NoArgsCommand):
    def handle_noargs (self, **options):
        # # # # # #
        # TRAITS  #
        # # # # # #

        trait_types = []
        traits = []

        for attr in dir(trait_models):
            if attr is 'EnumModel' or attr is 'TraitModel':
                continue

            Model = getattr(trait_models, attr)
            if not isinstance(Model, type):
                continue

            if issubclass(Model, trait_models.EnumModel):
                trait_types.append(Model)
            elif issubclass(Model, trait_models.TraitModel):
                traits.append(Model)

        for trait in traits:
            self.render(
                path.join(settings.PROJECT_PATH, 'traits', 'static', 'traits', 'coffeescript', 'models', to_underscores(trait._meta.object_name) + '.coffee'),
                'coffee', 'offline/coffee/backbone_model.coffee', { 'model': trait }
            )

        self.render(path.join(settings.PROJECT_PATH, 'traits', 'admin',       'trait_admins.py'),      'py', 'offline/py/admin.py',       { 'app_name': 'traits', 'models': traits })
        self.render(path.join(settings.PROJECT_PATH, 'traits', 'admin',       'enum_admins.py'),       'py', 'offline/py/admin_enum.py',  { 'app_name': 'traits', 'models': trait_types })
        self.render(path.join(settings.PROJECT_PATH, 'traits', 'serializers', 'trait_serializers.py'), 'py', 'offline/py/serializers.py', { 'app_name': 'traits', 'models': trait_types + traits })
        self.render(path.join(settings.PROJECT_PATH, 'traits', 'urls',        'traits_ajax.py'),       'py', 'offline/py/urls.py',        { 'app_name': 'traits', 'models': trait_types + traits })
        self.render(path.join(settings.PROJECT_PATH, 'traits', 'views',       'traits_ajax.py'),       'py', 'offline/py/views.py',       { 'app_name': 'traits', 'models': trait_types + traits })


        # # # # # # #
        # CHARACTER #
        # # # # # # #

        character_traits = []

        for attr in dir(character_models):
            if attr is 'Character' or attr is 'CharacterHasTraitModel':
                continue

            Model = getattr(character_models, attr)
            if not isinstance(Model, type):
                continue

            if issubclass(Model, character_models.CharacterHasTraitModel):
                character_traits.append(Model)

        Character = character_models.Character

        for character_trait in [ XPRecord ] + character_traits:
            self.render(
                path.join(settings.PROJECT_PATH, 'character', 'static', 'character', 'coffeescript', 'models', to_underscores(character_trait._meta.object_name) + '.coffee'),
                'coffee', 'offline/coffee/backbone_model.coffee', { 'model': character_trait }
            )

        self.render(path.join(settings.PROJECT_PATH, 'character', 'admin',       'character_trait_admins.py'),  'py', 'offline/py/admin.py',        { 'app_name': 'character', 'models': [            XPRecord ] + character_traits })
        self.render(path.join(settings.PROJECT_PATH, 'character', 'admin',       'character_traits_inline.py'), 'py', 'offline/py/admin_inline.py', { 'app_name': 'character', 'models': [            XPRecord ] + character_traits })
        self.render(path.join(settings.PROJECT_PATH, 'character', 'serializers', 'character_serializers.py'),   'py', 'offline/py/serializers.py',  { 'app_name': 'character', 'models': [ Character, XPRecord ] + character_traits })
        self.render(path.join(settings.PROJECT_PATH, 'character', 'urls',        'character_ajax.py'),          'py', 'offline/py/urls.py',         { 'app_name': 'character', 'models': [ Character, XPRecord ] + character_traits })
        self.render(path.join(settings.PROJECT_PATH, 'character', 'views',       'character_ajax.py'),          'py', 'offline/py/views.py',        { 'app_name': 'character', 'models': [ Character, XPRecord ] + character_traits })


        # # # # # # #
        # CHRONICLE #
        # # # # # # #

        chronicle_model_objects = [chronicle_models.Chronicle, chronicle_models.Game]

        for chronicle_model in chronicle_model_objects:
            self.render(
                path.join(settings.PROJECT_PATH, 'chronicle', 'static', 'chronicle', 'coffeescript', 'models', to_underscores(chronicle_model._meta.object_name) + '.coffee'),
                'coffee', 'offline/coffee/backbone_model.coffee', { 'model': chronicle_model }
            )

        self.render(path.join(settings.PROJECT_PATH, 'chronicle', 'admin',       'chronicle_admin.py'),       'py', 'offline/py/admin.py',        { 'app_name': 'chronicle', 'models': chronicle_model_objects })
        self.render(path.join(settings.PROJECT_PATH, 'chronicle', 'admin',       'chronicle_inline.py'),      'py', 'offline/py/admin_inline.py', { 'app_name': 'chronicle', 'models': [chronicle_models.Game] })
        self.render(path.join(settings.PROJECT_PATH, 'chronicle', 'serializers', 'chronicle_serializers.py'), 'py', 'offline/py/serializers.py',  { 'app_name': 'chronicle', 'models': chronicle_model_objects })
        self.render(path.join(settings.PROJECT_PATH, 'chronicle', 'urls',        'chronicle_ajax.py'),        'py', 'offline/py/urls.py',         { 'app_name': 'chronicle', 'models': chronicle_model_objects })
        self.render(path.join(settings.PROJECT_PATH, 'chronicle', 'views',       'chronicle_ajax.py'),        'py', 'offline/py/views.py',        { 'app_name': 'chronicle', 'models': chronicle_model_objects })


    def render (self, filepath, file_type, template_name, dictionary):
        content = render_to_string(template_name, dictionary)

        if path.exists(filepath):
            with open(filepath, 'r') as input:
                input.readline()
                line = input.readline().split('|')
                old_hash = '' if len(line) < 2 else line[1].strip()
        else:
            old_hash = ''

        new_hash = md5(content).hexdigest()
        if old_hash == new_hash:
            return

        print "generating '{}' ...".format(filepath)

        with open(filepath, 'wb') as out:
            out.write(render_to_string('offline/{file_type}/header.{file_type}'.format(file_type = file_type), {
                'timestamp': datetime.now(),
                'hash': new_hash,
            }))
            out.write(content)
