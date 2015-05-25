## @package DCMS.model_base
#  Defines base orm classes.


from sqlalchemy.ext.declarative import declarative_base

from dsqla.models import DjangoTablename, ToJSON


class BaseModel (DjangoTablename, ToJSON):
    pass


BaseModel = declarative_base(cls = BaseModel)
