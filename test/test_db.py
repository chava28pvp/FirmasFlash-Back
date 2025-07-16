import pytest
from sqlalchemy import create_engine, text
from app.config import settings


def test_connection(request):
    """Prueba la conexión a la base de datos principal"""
    print("\n🔍 Probando conexión a BD principal...")

    # Obtener la opción --test-env correctamente
    use_test_db = request.config.getoption("--test-env", default=False)
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