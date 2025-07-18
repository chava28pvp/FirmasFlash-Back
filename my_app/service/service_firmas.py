# services/firmas.py
from sqlalchemy.orm import Session
from my_app.models.firmas import typeArchive
from my_app.crud.firma_crud import create_firmas
from my_app.schemas.firmas_schemas import FirmasCreator, FirmasResponse


def create_firma_with_description(db: Session, data: FirmasCreator) -> FirmasResponse:
    firma = create_firmas(db, data)
    type_archive = db.query(typeArchive).filter(typeArchive.id == data.typeArchive).first()

    return FirmasResponse(
        name=firma.name,
        description=firma.description,
        typeArchiveDescription=type_archive.description if type_archive else None
    )
