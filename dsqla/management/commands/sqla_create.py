## @package dsqla.management.command.sqla_create
#  Defines the django management command for creating all the sqla-managed tables.


from django.conf import settings
from django.core.management.base import BaseCommand

from dsqla.session import session


class Command (BaseCommand):
    help = 'Creates all sqla-managed tables.'

    def handle (self, *args, **options):
        metadata = settings.DSQLA_BASE_MODEL.metadata
        metadata.create_all(session.bind)
