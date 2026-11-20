from fastapi import APIRouter,Depends
from service import auditlog
from core.database import get_db
from typing import List
from sqlalchemy.orm import Session
from schemas.auditlog import AuditCreate,AuditResponse
from core.secirity import get_current_user,role_required
from models.user import User 
admin_required=role_required("admin")



router=APIRouter(tags=["Auditlog"])



@router.patch("/admin/users/{user_id}/status",response_model=AuditResponse)
def status(user_id:int,data:AuditCreate,db:Session=Depends(get_db),current_user:User=Depends(admin_required)):
    return auditlog.change_status(user_id,db,current_user,data)


@router.get("/admin/users/{user_id}/status",response_model=List[AuditResponse])
def status(user_id:int,db:Session=Depends(get_db),current_user:User=Depends(admin_required)):
    return auditlog.show_audit(user_id,db)

