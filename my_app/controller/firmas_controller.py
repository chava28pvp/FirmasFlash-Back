# routers/firmas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from my_app.db.database import get_db
from my_app.schemas.firmas_schemas import FirmasCreator, FirmasResponse
from my_app.crud.firma_crud import create_firmas

router = APIRouter(prefix="/firmas", tags=["Firmas"])


@router.post("/", response_model=FirmasResponse)
def create_firma(data: FirmasCreator, db: Session = Depends(get_db)):
    try:
        return create_firmas(db, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
