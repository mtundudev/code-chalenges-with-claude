from models.user import User,StatusCheck
from models.auditlog import Auditlog
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from schemas.auditlog import AuditCreate

ALLOWED_TRANSITION={
    StatusCheck.pending:[
        StatusCheck.active,
        StatusCheck.deactivated
    ],
    StatusCheck.active:[
        StatusCheck.suspended,
        StatusCheck.deactivated
    ],
    StatusCheck.suspended:[
        StatusCheck.active,
        StatusCheck.deactivated
    ],
    StatusCheck.deactivated:[]
}


def change_status(user_id:int,db:Session,current_user:User,data:AuditCreate):
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user wiyh id of {user_id} not found")
    """check the user status in database (user.status) and perfom allowed transition """
    status=ALLOWED_TRANSITION[user.status]
    if data.status not in status:
        raise HTTPException(status_code=400,detail="invalid transition status")
    
    audit=Auditlog(
        user_id=user.id,
        actor_id=current_user.id,
        from_status=user.status,
        to_status=data.status,
        reason=data.reason
    )
    db.add(audit)

    user.status=data.status

    db.commit()
    db.refresh(user)
    db.refresh(audit)


    return audit


def show_audit(user_id:int,db:Session):
    audit=db.query(Auditlog).filter(Auditlog.user_id==user_id).all()
    if not audit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"audit with that user not found")
    return audit
