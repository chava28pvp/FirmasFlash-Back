from sqlalchemy.orm import Session
from my_app.models.firmas import usersAsignados
from my_app.schemas.users_schemas import userscreate


def create_users(db: Session, data: userscreate):
    new_user = usersAsignados(
        id_Firma=data.idFirma,
        usersAsignados=data.user,

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
