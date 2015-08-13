## @package DCMS.model_base
#  Defines base orm classes.


from sqlalchemy.ext.declarative import declarative_base

from dsqla.models import (
    # DjangoTablename, generate_table_to_model_map, MetaData, ToJSON
    BaseModelBase, DjangoTablename, MetaData, TableToModelMap, ToJSON
)


class BaseModel (DjangoTablename, TableToModelMap, ToJSON, BaseModelBase):
    pass


BaseModel = declarative_base(cls = BaseModel, metadata = MetaData())
# generate_table_to_model_map(BaseModel)
