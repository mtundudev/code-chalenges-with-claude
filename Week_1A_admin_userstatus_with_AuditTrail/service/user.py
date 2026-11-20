from schemas.user import UserCreate,UserUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from models.userRole import UserRole
from models import Role
from models.user import User
from core.secirity import Hashing,create_access_token



class UserServices:
    def login(email:str,password:str,db:Session):
        user=db.query(User).filter(User.email==email).first()
        if not (user or Hashing.verify(password,user.password) ):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="wrong email or password")

        token=create_access_token({"sub":user.email})

        return {
            "access_token":token,
            "token_type":"Bearer"
        }

    def user_create(db:Session,data:UserCreate):
        exit= db.query(User).filter(User.email==data.email).first()
        if exit:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="email already exist")

        roles=db.query(Role).filter(Role.name=="admin").first()

        user=User(
            fullname=data.fullname,
            password=Hashing.Hash(data.password),
            email=data.email,
            role=roles.name

        )
        db.add(user)
        db.flush()

        userrole=UserRole(
            User_id=user.id,
            role_id=roles.id
        )
        db.add(userrole)
        
        db.commit()
        db.refresh(user)

        return user


    def user_list(db:Session):
        user=db.query(User).all()
        return user

    def user_id(user_id,db:Session):
        user=db.query(User).filter(User.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"user withn id of {user_id} not found")
        return user

    def update_user(user_id,db:Session,data:UserUpdate):
        user=db.query(User).filter(User.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"user with id of {user_id} no found")

        if user.email==data.email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="conflict email already exist")
        user.fullname=data.fullname
        user.email=data.email
        user.password=data.password

        db.commit()
        db.refresh(user)
        return user
    
    def delete_user(user_id,db:Session):
        user=db.query(User).filter(User.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"user with id of {user_id} not found") 
        db.delete(user)
        db.commit()


        return {
            "message":"user deleted successfuly"
        }   
