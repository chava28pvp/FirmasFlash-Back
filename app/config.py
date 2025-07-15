from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv
import urllib.parse

load_dotenv()
class Settings(BaseSettings):
    DB_SERVER: str = Field(default="GAMEZ28\SQLEXPRESS")
    DB_NAME: str = Field(default="firmasConnection")
    DB_USER: str = Field(default="")
    DB_PASSWORD: str = Field(default="")
    TRUSTED_CONNECTION: str = Field(default="yes")
    DB_DRIVER: str = Field(default="ODBC Driver 17 for SQL Server")

    @property
    def DATABASE_URL(self) -> str:
        driver_escaped = urllib.parse.quote_plus(self.DB_DRIVER)
        if self.TRUSTED_CONNECTION.lower() == "yes":
            return f"mssql+pyodbc://{self.DB_SERVER}/{self.DB_NAME}?driver={driver_escaped}&trusted_connection=yes"
        return f"mssql+pyodbc://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_SERVER}/{self.DB_NAME}?driver={driver_escaped}"

    class Config:  # ← Clase Config interna para configuración de Pydantic
        env_file = ".env"  # Nombre del archivo .env a buscar
        env_file_encoding = 'utf-8'  # Codificación del archivo
        extra = 'ignore'


settings = Settings()
