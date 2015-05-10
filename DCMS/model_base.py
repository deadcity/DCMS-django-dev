## @package DCMS.model_base
#  Defines base orm classes.


from sqlalchemy.ext.declarative import declartive_base

from dsqla.models import DjangoTablename, ToJSON


class Base (DjangoTablename, ToJSON):
    pass


Base = declartive_base(cls = Base)
