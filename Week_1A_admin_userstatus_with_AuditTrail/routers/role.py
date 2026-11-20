from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from core.database import get_db
from service.seed import seed

router=APIRouter(prefix="/role",tags=["Seed"])


@router.post("")
def seedrole(db:Session=Depends(get_db)):
    return seed(db)