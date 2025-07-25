from sqlalchemy.orm import Session
from my_app.models.firmas import archiveURL
from my_app.schemas.archive_schemas import archivecreate


def create_archive(db: Session, data: archivecreate):
    new_archive = archiveURL(
        path_file=data.pathFile,
        firma_id=data.idFirma,

    )
    db.add(new_archive)
    db.commit()
    db.refresh(new_archive)

    return new_archive
