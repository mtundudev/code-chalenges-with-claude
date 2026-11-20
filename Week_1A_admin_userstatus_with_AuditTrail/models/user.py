from core.database import Base
from sqlalchemy import Column,DateTime,String,Integer,Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

class StatusCheck(str,enum.Enum):
    pending="PENDING"
    active="ACTIVE"
    suspended="SUSPENDED"
    deactivated="DEACTIVATED"

class User(Base):
    __tablename__ ="users"

    id=Column(Integer,primary_key=True)
    fullname=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    status=Column(Enum(StatusCheck),default=StatusCheck.pending)
    role=Column(String,nullable=True)
    version=Column(Integer)
    created_at=Column(DateTime,default=datetime.now())
    updated_at=Column(DateTime,onupdate=datetime.now())

    audit=relationship("Auditlog",back_populates="user")
    