from sqlalchemy.orm import Session
from app.models.firmas import firmas


def create_firmas(db: Session, firmas_data: dict):
    db_firmas = firmas(**firmas_data)
    db.add(db_firmas)
    db.commit()
    db.refresh(db_firmas)
    return db_firmas
