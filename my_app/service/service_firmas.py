# services/firmas.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from my_app.models.firmas import typeArchive
from my_app.crud.firma_crud import create_firmas
from my_app.schemas.firmas_schemas import FirmasCreator, FirmasResponse


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