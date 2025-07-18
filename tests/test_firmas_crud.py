
from my_app import create_firmas
from my_app import typeArchive
from my_app import FirmasCreator


# $env:PYTHONPATH="."; pytest tests/unit/test_firmas_crud.py
def test_create_firma_crud(db_session):
    firma_data = {
        "Name_firma": "Firma Test",
        "Description_firma": "Test firma desc",
        "upload_by": "tester",  # Solo si tu esquema lo espera
        "typeArchive": 1
    }

    # Crea una entrada en la tabla typeArchive primero
    db_session.add(typeArchive(id=1, description="PDF"))
    db_session.commit()

    response = create_firmas(db_session, FirmasCreator(**firma_data))
    db_session.refresh(response)

    assert response.name == "Firma Test"
    assert response.description == "Test firma desc"
    assert response.type_archive.description == "PDF"
