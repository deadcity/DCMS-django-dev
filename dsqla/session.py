## @package dsqla.session
#  Defines basic tools for initiating a session based on Django database
#  configuration and provides a default session.


from django.conf import settings

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm.session import sessionmaker


Session = sessionmaker()
_sessions = {}


ENGINE = {
    'sqlite3'             : 'sqlite',
    'mysql'               : 'mysql',
    'postgresql'          : 'postgresql',
    'postgresql_psycopg2' : 'postgresql+psycopg2',
    'oracle'              : 'oracle',
}


def get_session (database_alias = 'default'):
    _session = _sessions.get(database_alias, None)

    if _session is None:
        db_settings = settings.DATABASES[database_alias]
        engine = create_engine(URL(
            ENGINE[db_settings['ENGINE'].split('.')[-1]],
            username = db_settings['USER'],
            password = db_settings['PASSWORD'],
            host     = db_settings['HOST'],
            port     = db_settings['PORT'],
            database = db_settings['NAME']
        ), echo = settings.DEBUG)

        _sessions[database_alias] = _session = Session(bind = engine)

    return _session


session = get_session()
