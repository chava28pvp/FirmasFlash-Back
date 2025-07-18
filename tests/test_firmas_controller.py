from my_app import typeArchive


def test_create_firma_endpoint(test_client, db_session):
    # Arrange: preparar los datos necesarios
    db_session.add(typeArchive(id=1, description="PDF"))
    db_session.commit()

    payload = {
        "Name_firma": "Firma Test",
        "Description_firma": "Descripción de prueba",
        "typeArchive": 1
    }

    # Act: llamar al endpoint
    response = test_client.post("/firmas/", json=payload)

    # Assert: verificar la respuesta
    assert response.status_code == 200, f"Error: {response.text}"

    data = response.json()
    assert data["name"] == "Firma Test"
    assert data["description"] == "Descripción de prueba"
    assert data["typeArchiveDescription"] == "PDF"
