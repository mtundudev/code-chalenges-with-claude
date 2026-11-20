from core.database import Base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__="roles"

    id=Column(Integer,primary_key=True)
    name=Column(String,unique=True)

    userroles=relationship("UserRole",back_populates="role")

