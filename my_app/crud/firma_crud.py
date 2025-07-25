from typing import Optional, List
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


def get_firma(db: Session, firma_id: int):
    return db.query(firmas).filter(firmas.id == firma_id).first()


def get_all_firmas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(firmas).offset(skip).limit(limit).all()


def update_firma(db: Session, firma_id: int, **kwargs):
    db_firma = get_firma(db,firma_id)
    if not db_firma:
        return None

    for key, value in kwargs.items():
        setattr(db_firma, key, value)

    db.commit()
    db.refresh(db_firma)
    return db_firma


def delete_firma(db: Session, firma_id: int):
    db_firma = get_firma(db, firma_id)
    if not db_firma:
        return False

    db.delete(db_firma)
    db.commit()
    return True
