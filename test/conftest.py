import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base
from app.config import settings
from dotenv import load_dotenv


load_dotenv('.env')


@pytest.fixture(scope="session")
def engine():
    """Fixture para el motor de pruebas"""
    test_db_url = f"{settings.DATABASE_URL}_test"
    engine = create_engine(test_db_url)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture
def db_session(engine):
    """Fixture para sesiones de prueba"""
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session

    session.close()
    transaction.rollback()
    connection.close()