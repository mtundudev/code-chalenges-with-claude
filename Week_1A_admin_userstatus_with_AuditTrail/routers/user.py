from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import UserResponse,UserCreate,UserUpdate
from service.user import UserServices
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List
from core.secirity import get_current_user,role_required

admin_required=role_required("admin")

router= APIRouter(prefix="/user",tags=["User"])


@router.post("/login")
def login_user(db:Session=Depends(get_db),data:OAuth2PasswordRequestForm=Depends()):
    return UserServices.login(data.username,data.password,db)

@router.post("/",response_model=UserResponse)
def user_create(data:UserCreate,db:Session=Depends(get_db)):
    return UserServices.user_create(db,data)

@router.get("/",response_model=List[UserResponse])
def user_list(db:Session=Depends(get_db),current_user=Depends(admin_required)):
    return UserServices.user_list(db)

@router.get("/{user_id}",response_model=UserResponse)
def user_id(user_id:int,db:Session=Depends(get_db)):
    return UserServices.user_id(user_id,db)

@router.put("/{user_id}",response_model=UserResponse)
def user_update(user_id:int,data:UserUpdate,db:Session=Depends(get_db)):
    return UserServices.update_user(user_id,db,data)

@router.delete("/{user_id}")
def user_delete(user_id:int,db:Session=Depends(get_db)):
    return UserServices.delete_user(user_id,db)