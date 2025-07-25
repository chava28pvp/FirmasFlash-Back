from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from my_app.db.database import get_db
from my_app.schemas.users_schemas import userscreate, usersresponse
from my_app.service.service_users import create_users_group

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", response_model=usersresponse)
def create_firma(data: userscreate, db: Session = Depends(get_db)):
    try:
        return create_users_group(db, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
