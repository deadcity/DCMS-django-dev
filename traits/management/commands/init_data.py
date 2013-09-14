from django.core.management.base import NoArgsCommand, CommandError
from django.db.models.loading import get_model
from django.db.utils import IntegrityError

from traits.management.data import enums, traits
from traits.models import *


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        for model_name, data in enums.items():
            self.stdout.write('Creating records for traits.' + model_name + '\n')
            Model = get_model('traits', model_name)
            for datum in data:
                record = Model(**datum)
                try:
                    record.save()
                except IntegrityError:
                    pass

        for model_name, data in traits.items():
            self.stdout.write('Creating records for traits.' + model_name + '\n')
            Model = get_model('traits', model_name)
            for datum in data:
                if 'type' in datum and datum['type']:
                    datum['type'] = next(f.related.parent_model.objects.get(name = datum['type'])
                                         for f in Model._meta.fields
                                         if f.name == 'type')
                record = Model(**datum)
                try:
                    record.save()
                except IntegrityError:
                    pass
