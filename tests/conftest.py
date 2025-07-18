import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from my_app import Base, get_db
from my_app import settings
from my_app import app


@pytest.fixture(scope="function")
def db_session():
    # Crear engine SQLite en memoria o en archivo de test
    engine = create_engine(settings.TEST_DB1_URL)

    # Crear todas las tablas antes de test
    Base.metadata.create_all(bind=engine)

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.rollback()  # Revertir cambios en sesión activa
        db.close()  # Cerrar sesión
        Base.metadata.drop_all(bind=engine)  # Eliminar tablas después del test


@pytest.fixture(scope="function")
def test_client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
