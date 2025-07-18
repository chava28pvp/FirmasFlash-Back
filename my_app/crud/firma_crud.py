from sqlalchemy.orm import Session
from my_app.models.firmas import firmas
from my_app.schemas.firmas_schemas import FirmasCreator


def create_firmas(db: Session, data: FirmasCreator):
    new_firma = firmas(
        name=data.Name_firma,
        description=data.Description_firma,
        type_archive_id=data.typeArchive,
        upload_by="system"  # o algún usuario actual
    )
    db.add(new_firma)
    db.commit()
    db.refresh(new_firma)

    return new_firma
