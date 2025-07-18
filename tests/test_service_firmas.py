from my_app import create_firma_with_description
from my_app import typeArchive
from my_app import FirmasCreator


def test_create_firma_with_description(db_session):
    # Preparamos un tipo de archivo
    db_session.add(typeArchive(id=1, description="PDF"))
    db_session.commit()

    # Datos de prueba
    data = FirmasCreator(
        Name_firma="Firma Test",
        Description_firma="Una firma de prueba",
        typeArchive=1
    )

    # Ejecutamos el servicio
    result = create_firma_with_description(db_session, data)

    # Validamos la respuesta
    assert result.name == "Firma Test"
    assert result.description == "Una firma de prueba"
    assert result.typeArchiveDescription == "PDF"
