from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Usa la propiedad DATABASE_URL correctamente
engine = create_engine(
    settings.DATABASE_URL,  # Accede a la propiedad, no al método
    pool_pre_ping=True,
    connect_args={
        "timeout": 30,
        "autocommit": True
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

Base = declarative_base()
