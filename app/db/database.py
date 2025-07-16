from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config import settings

# Motor principal con Trusted Connection
engine = create_engine(
    settings.DB1_URL,
    pool_pre_ping=True,
    connect_args={}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
