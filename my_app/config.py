from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache
import os
from dotenv import load_dotenv

# Cargar variables de entorno primero
load_dotenv()


class Settings(BaseSettings):
    DB1_URL: str = Field(..., description="Cadena de conexión para SQL Server")

    # Configuración para testing (con valor por defecto)
    TEST_DB1_URL: str = Field(
        default="sqlite:///./test.db",
        description="Cadena de conexión para testing"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
