from pydantic import BaseModel


class archivecreate(BaseModel):
    idFirma: int
    pathFile: str
