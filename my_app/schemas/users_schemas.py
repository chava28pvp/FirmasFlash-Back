from pydantic import BaseModel


class userscreate(BaseModel):
    idFirma: int
    user: str
