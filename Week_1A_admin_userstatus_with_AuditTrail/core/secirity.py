from pwdlib import PasswordHash
from datetime import datetime,timedelta
from core.config import settings
from jose import jwt,JWTError
from sqlalchemy.orm import Session
from core.database import get_db
from models.user import User
from models.role import Role
from models.userRole import UserRole
from fastapi import HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_schema=OAuth2PasswordBearer(tokenUrl="/user/login")



pass_hash=PasswordHash.recommended()



class Hashing:
    def Hash(password):
        return pass_hash.hash(password)

    def verify(plain_passwprd,hashed_password):
        return pass_hash.verify(plain_passwprd,hashed_password)

def create_access_token(data:dict):
    to_encode=data.copy()
    expire_time=datetime.now() +timedelta(minutes=settings.EXPIRE_ACCESS_TOKEN)
    to_encode.update({"exp":expire_time})

    token= jwt.encode(to_encode,settings.JWT_SECRET,algorithm=settings.ALGORITHM)

    return token

def decode_token(token:str):
    try:
        payload=jwt.decode(token,settings.JWT_SECRET,algorithms=[settings.ALGORITHM])
        return payload

    except JWTError:
        return None
        
    

def get_current_user(token:str=Depends(oauth2_schema),db:Session=Depends(get_db)):
    payload=decode_token(token)

    if not payload:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid or expired token")
    
    user_id=payload.get("sub")  
    if not user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="token has no user information")
     
    user=db.query(User).filter(User.email==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user info not found")
    return user


def role_required(requied_role:str):
    def role_check(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
        roles=db.query(Role.name).join(UserRole,
                                       UserRole.role_id==Role.id
                                       ).filter(UserRole.User_id==current_user.id).all()

        role_name=[ur.name for ur in roles]

        if "admin" in role_name:
            return current_user
        if requied_role not in role_name:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="access denied")
        return current_user
    return role_check



