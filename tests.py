from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_check_data():
    params = {'phone': '1'}
    response = client.get('/check_data',
                          params=params)
    assert response.status_code == 200


def test_write_data():
    json = {'phone': '1',
            'address': 'test'}
    response = client.post('/write_data',
                           json=json)
    assert response.status_code == 200