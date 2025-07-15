from sqlalchemy import text  # Importa text de SQLAlchemy


def test_database_connection(engine):
    """Prueba que la conexión a la base de datos funciona"""
    with engine.connect() as connection:
        # Usa text() para crear una expresión SQL ejecutable
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1


def test_create_user(db_session):
    """Prueba operaciones básicas con la sesión"""
    from app.db.models import User  # Asegúrate de importar tu modelo

    # Test de creación
    new_user = User(email="test@example.com")
    db_session.add(new_user)
    db_session.commit()

    # Test de lectura
    user = db_session.query(User).filter_by(email="test@example.com").first()
    assert user is not None
    assert user.email == "test@example.com"
