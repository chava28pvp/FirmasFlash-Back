import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


@pytest.fixture(scope="session")
def db_engine():
    """Fixture para el motor de base de datos"""
    db_url = settings.DB1_URL if not hasattr(pytest, "testing_env") else settings.TEST_DB1_URL
    engine = create_engine(db_url)

    yield engine

    engine.dispose()


@pytest.fixture
def db_session(db_engine):
    """Fixture para sesiones de base de datos"""
    Session = sessionmaker(bind=db_engine)
    session = Session()

    yield session

    session.rollback()
    session.close()


def pytest_configure(config):
    """Configuración global de pytest"""
    pytest.testing_env = config.getoption("--test-env")


def pytest_addoption(parser):
    """Añadir opción de línea de comandos"""
    parser.addoption(
        "--test-env",
        action="store_true",
        default=False,
        help="Usar configuración de testing"
    )
