from pydantic import BaseModel


class userscreate(BaseModel):
    idFirma: int
    user: str


class usersresponse(BaseModel):
    user: str
