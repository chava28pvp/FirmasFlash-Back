from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from my_app.db.database import get_db
from my_app.schemas.archive_schemas import archiveresponse, archivecreate
from my_app.service.service_archive import create_archive_id

router = APIRouter(prefix="/archive", tags=["Archive"])


@router.post("/", response_model=archiveresponse)
def create_firma(data: archivecreate, db: Session = Depends(get_db)):
    try:
        return create_archive_id(db, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
