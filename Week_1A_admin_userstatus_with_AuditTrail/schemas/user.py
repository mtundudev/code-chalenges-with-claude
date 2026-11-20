from pydantic import BaseModel,EmailStr
from typing import Optional
from models.user import StatusCheck
from datetime import datetime

class UserCreate(BaseModel):
    fullname:str
    email:EmailStr
    password:str


class UserUpdate(BaseModel):
    fullname:Optional[str]=None
    email:Optional[EmailStr]=None
    password:Optional[str ]=None   

class UserResponse(BaseModel):
    id:int
    fullname:str
    email:str
    version:Optional[int]=None
    role:Optional[str]=None
    status:StatusCheck
    created_at:Optional[datetime]=None
    updated_at:Optional[datetime]=None
