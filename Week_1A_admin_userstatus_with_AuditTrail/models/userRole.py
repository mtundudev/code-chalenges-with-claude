from core.database import Base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship


class UserRole(Base):
    __tablename__="userroles"

    id=Column(Integer,primary_key=True)
    User_id=Column(Integer)
    role_id=Column(Integer,ForeignKey("roles.id"))


    role=relationship("Role",back_populates="userroles")
    