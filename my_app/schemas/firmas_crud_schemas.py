from typing import List
from pydantic import BaseModel, ConfigDict
from datetime import datetime


# Schemas para las relaciones
class ArchiveURLResponse(BaseModel):
    id: int
    path_file: str

    class Config:
        orm_mode = True


class UserAsignadoResponse(BaseModel):
    id: int
    usuario: str

    class Config:
        orm_mode = True


class TypeArchiveResponse(BaseModel):
    id: int
    description: str
    creation_date: datetime

    class Config:
        orm_mode = True


# Schema principal
class FirmasFullResponse(BaseModel):
    id: int
    name: str
    description: str
    active: bool
    upload_by: str
    type_archive: TypeArchiveResponse  # Relación con typeArchive
    archive_urls: List[ArchiveURLResponse]  # Lista de archivos relacionados
    users_asignados: List[UserAsignadoResponse]  # Lista de usuarios asignados

    model_config = ConfigDict(from_attributes=True)  # Esto es lo nuevo en Pydantic v2

