from pydantic import BaseModel


class FirmasCreator(BaseModel):
    Name_firma: str
    Description_firma: str
    typeArchive: int


class FirmasResponse(BaseModel):
    name: str
    description: str
    typeArchiveDescription: str
