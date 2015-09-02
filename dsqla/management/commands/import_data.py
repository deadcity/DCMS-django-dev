## @package dsqla.management.command.import_data
#  Defines a django management command for importing data.


from collections import OrderedDict
import json

from django.core.management.base import BaseCommand

from sqlalchemy.sql.schema import UniqueConstraint

from dsqla.models import get_model
from dsqla.session import session


def prepare (session, Model, datum):
    datum = dict(datum)

    # Retrieve referenced models.
    for relationship in Model.__mapper__.relationships:
        if relationship.key in datum:
            RelatedModel = relationship.mapper.class_
            related_datum = prepare(session, RelatedModel,
                datum[relationship.key])

            related_model = (session
                .query(RelatedModel)
                .filter(*[
                    getattr(RelatedModel, field) == value
                    for field, value
                    in related_datum.items()
                ])
                .one()
            )

            datum[relationship.key] = related_model

    return datum


def key_from_constraint (constraint, obj):
    if isinstance(obj, dict):
        return tuple(
            obj[column.key[:-3]].id
                if column.key.endswith('_id')
                else column.key
            for column
            in constraint.columns
        )
    else:
        return tuple(
            getattr(obj, column.key[:-3]).id
                if column.key.endswith('_id')
                else getattr(column.key)
            for column
            in constraint.columns
        )


def filter_from_constraint (constraint, obj):
    if isinstance(obj, dict):
        return tuple(
            column == (
                obj[column.key[:-3]].id
                if column.key.endswith('_id')
                else obj[column.key]
            )
            for column
            in constraint.columns
        )
    else:
        return tuple(
            column == (
                getattr(obj, column.key[:-3]).id
                if column.key.endswith('_id')
                else getattr(obj, column.key)
            )
            for column
            in constraint.columns
        )


class Command (BaseCommand):
    help = 'Import data for application from file.'

    def add_arguments (self, parser):
        parser.add_argument('filepath')
        parser.add_argument('--debug', action = 'store_true')

    def handle (self, *args, **options):
        session.bind.echo = options['debug']
        filepath = options['filepath']

        model_info = {}

        with open(filepath, 'r') as data_file:
            content = ''.join(line.split('//')[0] for line in data_file)
            full_data = json.loads(content, object_pairs_hook = OrderedDict)

        for data_block in full_data:
            Model = get_model(data_block['application'], data_block['Model'])
            unique_indexes = {}

            # Prepare indeces of unique-constraints.
            for table in Model.__mapper__.tables:
                for constraint in table.constraints:
                    if isinstance(constraint, UniqueConstraint):
                        unique_indexes[constraint] = set()

            for datum in data_block['data']:
                datum = prepare(session, Model, datum)
                update_target = None

                for constraint, index in unique_indexes.items():
                    # Look for item in index.
                    key = key_from_constraint(constraint, datum)
                    if key in index:
                        self.stderr.write("ERROR: Second import of '{}' " +
                            "record with unique constraint:".format(Model))
                        for column, value in zip(constraint.columns, key):
                            self.stderr.write("       {} = {}".format(
                                column, value))
                        return

                    # Look for item in database.
                    target = session.query(Model).filter(
                        *filter_from_constraint(constraint, datum)).scalar()
                    if update_target and update_target != target:
                        self.stderr.write('ERROR: Second unique-index match does not yield the same model.')
                        self.stderr.write("       Model: {}".format(Model))
                        self.stderr.write("       constraint: {}".format(constraint))
                        self.stderr.write("       data: {}".format(datum))
                        return
                    update_target = target

                if update_target:
                    updated = False
                    for field, value in datum.items():
                        if getattr(update_target, field) != value:
                            updated = True
                            setattr(update_target, field, value)
                    if updated:
                        self.stdout.write("updating {}".format(update_target))
                else:
                    model = Model(**datum)
                    session.add(model)
                    self.stdout.write("adding {}".format(model))

            session.flush()

        session.commit()
