from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional as Optional1


class Settings(BaseSettings):
    DB_SERVER: str = Field(default="GAMEZ28\SQLEXPRESS", env="DB_SERVER")
    DB_NAME: str = Field(default="firmasConnection", env="DB_NAME")
    DB_USER: Optional1[str] = Field(default=None, env="DB_USER")
    TRUSTED_CONNECTION: str = Field(default=None, env="DB_PASSWORD")
    DB_PASSWORD: Optional1[str] = Field(dafault="yes", env="TRUSTED_CONNECTION")

    @property
    def DATABASE_URL(self) -> str:
        if Settings.TRUSTED_CONNECTION.lower() == "yes":
            return (
                f"mssql+pyodbc://{self.DB_SERVER}/{self.DB_NAME}"
                f"?driver=ODBC+Driver+17+for+SQL+Server"
                f"&trusted_connection=yes"
            )
        else:
            return (
                f"mssql+pyodbc://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_SERVER}/{self.DB_NAME}"
                f"?driver=ODBC+Driver+17+for+SQL+Server"
            )

    class config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
