from fastapi import HTTPException
from sqlalchemy.orm import Session
from my_app.crud.archive_crud import create_archive
from my_app.schemas.archive_schemas import archivecreate, archiveresponse


def create_archive_id(db: Session, data: archivecreate):
    archive = create_archive(db, data)

    return archiveresponse(
        id=archive.id
    )
