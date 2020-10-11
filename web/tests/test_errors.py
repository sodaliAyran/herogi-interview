import pytest

def test_get_values(client):
    response = client.get("/get_values")
    assert response != None

def test_four_oh_four(client):
    response = client.get("/none_existing_endpoint")
    assert response.status_code == 404
