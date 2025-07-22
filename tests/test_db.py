import pytest
from sqlalchemy import create_engine, text
from my_app.config import settings
from my_app.models.firmas import typeArchive


def test_connection(request):
    """Prueba la conexión a la base de datos principal"""
    print("\n🔍 Probando conexión a BD principal...")

    # Obtener la opción --tests-env correctamente
    use_test_db = request.config.getoption("--tests-env", default=False)
    db_url = settings.TEST_DB1_URL if use_test_db else settings.DB1_URL

    print(f"📌 URL de conexión: {db_url}")

    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            # Consulta diferente para SQLite vs SQL Server
            if "sqlite" in db_url:
                result = conn.execute(text("SELECT 1"))
            else:
                result = conn.execute(text("SELECT @@version as version"))
                version = result.scalar()
                print(f"🛠️ Versión de SQL Server: {version}")

            assert result is not None
        print("✅ Conexión exitosa!")
        return True
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        pytest.fail(f"Error de conexión: {e}")
        return False


def test_insert_and_query_typearchive(db_session):
    # Crear una nueva entrada
    new_type = typeArchive(id=1, description="Prueba ORM")
    db_session.add(new_type)
    db_session.commit()

    # Consultar la entrada creada
    queried = db_session.query(typeArchive).filter_by(id=1).first()

    assert queried is not None
    assert queried.description == "Prueba ORM"

    # Opcional: limpiar base de datos después del test
    db_session.delete(queried)
    db_session.commit()


