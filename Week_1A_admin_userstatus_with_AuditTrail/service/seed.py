from sqlalchemy.orm import Session
from models.role import Role
from fastapi import HTTPException,status

roles=[
    {"name":"user"},
    {"name":"admin"},
    {"name":"staff"}
]


def seed(db:Session):
    for data in roles:
        role=db.query(Role).filter(Role.name==data["name"]).all()
        if role:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="already role created")
            continue
        role=Role(
            name=data["name"]
        )
        db.add(role)
    db.commit()  
    return{
        "message":"successfuly role created"
    }  