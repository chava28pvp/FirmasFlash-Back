from pydantic import BaseModel


class FirmasCreator(BaseModel):
    Name_firma: str
    Description_firma: str
    typeArchive: str


class FirmasResponse(FirmasCreator):
    Name_firma: str
    Description_firma: str
