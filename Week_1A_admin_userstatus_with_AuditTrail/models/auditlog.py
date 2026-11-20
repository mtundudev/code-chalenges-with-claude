from core.database import Base
from sqlalchemy import Column,String,ForeignKey,DateTime,Integer,Enum
from sqlalchemy.orm import relationship
from models.user import StatusCheck
from datetime import datetime


class Auditlog(Base):
    __tablename__="auditlogs"

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    actor_id=Column(Integer)
    from_status=Column(Enum(StatusCheck))
    to_status=Column(Enum(StatusCheck))
    reason=Column(String)
    created_at=Column(DateTime,default=datetime.now())


    user=relationship("User",back_populates="audit")