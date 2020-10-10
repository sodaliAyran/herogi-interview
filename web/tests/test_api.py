import pytest

def test_api_check(client):
    response = client.get('/')
    assert response.status_code == 200

def test_get_get_values_return_four_oh_five(client):
    response = client.get('/get_values')
    assert response.status_code == 405
