## @package dsqla.middleware
#  Django middleware


from django_sqla.session import session


class SQLATransactionMiddleware (object):
    def process_response (self, request, response):
        session.commit()
        return response

    def process_exception (self, request, exception):
        session.rollback()