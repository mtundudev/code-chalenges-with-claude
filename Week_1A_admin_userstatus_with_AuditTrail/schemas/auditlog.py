from pydantic import BaseModel
from models.user import StatusCheck
from typing import Optional
from datetime import datetime


class AuditCreate(BaseModel):
    status:StatusCheck
    reason:str
    expected_version:Optional[int]=None


class AuditResponse(BaseModel):
    id:int
    user_id:int
    actor_id:int
    reason:str
    from_status:StatusCheck
    to_status:StatusCheck
    created_at:datetime