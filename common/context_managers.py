from django.core.exceptions import PermissionDenied


class db_user(object):
    def __init__(self, connection, new_user):
        # print '  db_user.__init__ -', new_user
        if new_user == '':
            raise PermissionDenied
        self._cursor = connection.cursor()
        self._new_user = new_user

    def __enter__(self):
        # print '  db_user.__enter__ -', self.new_user
        self._cursor.execute('SELECT current_user')
        self._old_user = self._cursor.fetchone()[0]
        self._set_role(self.new_user)

    def __exit__(self, exc_type, exc_value, traceback):
        # print '  db_user.__exit__ -', self.new_user
        self._set_role(self.old_user)

    def _set_role(self, user):
        self._cursor.execute('SET ROLE %s', [user])

    @property
    def new_user(self):
        return self._new_user

    @property
    def old_user(self):
        return self._old_user
