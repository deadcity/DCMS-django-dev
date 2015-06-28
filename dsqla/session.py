## @package dsqla.session
#  Defines basic tools for initiating a session based on Django database
#  configuration and provides a default session.


from django.conf import settings

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker


_session_classes = {}


ENGINE = {
    'sqlite3'             : 'sqlite',
    'mysql'               : 'mysql',
    'postgresql'          : 'postgresql',
    'postgresql_psycopg2' : 'postgresql+psycopg2',
    'oracle'              : 'oracle',
}


def get_session (database_alias = 'default'):
    Session = _session_classes.get(database_alias, None)

    if Session is None:
        db_settings = settings.DATABASES[database_alias]
        port = db_settings['PORT']

        engine = create_engine(URL(
            ENGINE[db_settings['ENGINE'].split('.')[-1]],
            username = db_settings['USER'],
            password = db_settings['PASSWORD'],
            host     = db_settings['HOST'],
            port     = None if port == '' else port,
            database = db_settings['NAME']
        ), echo = settings.DEBUG)

        session_factory = sessionmaker(bind = engine)
        Session = scoped_session(session_factory)
        _session_classes[database_alias] = Session

    return Session


session = get_session()
