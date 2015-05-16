## @module auth.models


from sqlalchemy.schema import Column
from sqlalchemy.types import Boolean, DateTime, Integer, String

from DCMS.model_base import BaseModel

from dsqla.models import app_label


AppLabel = app_label('auth')


class User (AppLabel, BaseModel):
    username   = Column(String(30), nullable = False, unique = True)
    first_name = Column(String(30), nullable = False, default = '')
    last_name  = Column(String(30), nullable = False, default = '')
    email      = Column(String(254), nullable = False, default = '')

    # password = Column(String(128), nullable = False)

    is_staff     = Column(Boolean, nullable = False, default = False)
    is_active    = Column(Boolean, nullable = False, default = True)
    is_superuser = Column(Boolean, nullable = False, default = False)

    last_login  = Column(DateTime)
    date_joined = Column(DateTime, nullable = False)
