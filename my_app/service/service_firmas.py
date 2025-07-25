# services/firmas.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from my_app.models.firmas import typeArchive
from my_app.crud.firma_crud import create_firmas, get_firma, get_all_firmas, update_firma, delete_firma
from my_app.schemas.firmas_schemas import FirmasCreator, FirmasResponse
from my_app.schemas.firmas_crud_schemas import FirmasFullResponse
from my_app.models import firmas
from typing import List


def create_firma_with_description(db: Session, data: FirmasCreator) -> FirmasResponse:
    firma = create_firmas(db, data)
    type_archive = db.query(typeArchive.description).filter(typeArchive.id == data.typeArchive).scalar()

    if not type_archive:
        raise HTTPException(status_code=404, detail="Tipo de archivo no encontrado")
    return FirmasResponse(
        name=firma.name,
        description=firma.description,
        typeArchiveDescription=str(type_archive)
    )


def get_firma_service(db: Session, firma_id: int) -> firmas:
    return get_firma(db, firma_id)


def get_all_firmas_service(db: Session, skip: int = 0, limit: int = 100) -> List[firmas]:
    return get_all_firmas(db, skip, limit)


def update_firma_service(db: Session, firma_id: int, firma_data: dict) -> firmas:
    return update_firma(db, firma_id, **firma_data)


def delete_firma_service(db: Session, firma_id: int) -> bool:
    return delete_firma(db, firma_id)


def to_full_response(db_firma: firmas) -> FirmasFullResponse:
    return FirmasFullResponse.from_orm(db_firma)
