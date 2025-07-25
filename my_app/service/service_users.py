from fastapi import HTTPException
from sqlalchemy.orm import Session
from my_app.crud.users_crud import create_users
from my_app.schemas.users_schemas import userscreate, usersresponse


def create_users_group(db: Session, data: userscreate):
    users = create_users(db, data)

    return usersresponse(
        user=users.usuario
    )
