from fastapi.testclient import TestClient
from main import app, redis

client = TestClient(app)


def test_check_data():
    phone = '89090000000'
    address = 'текстовый адрес'
    params = {'phone': phone}
    redis.set(name=phone,
              value=address)
    response = client.get('/check_data',
                          params=params)
    assert response.status_code == 200
    assert response.json() == address


def test_write_data():
    phone = '89090000000'
    address = 'текстовый адрес'
    redis.set(name=phone,
              value=address)
    expected_address = 'текстовый адрес 1'
    json = {'phone': phone,
            'address': expected_address}
    response = client.post('/write_data',
                           json=json)
    real_address = redis.get(name=phone)

    assert response.status_code == 200
    assert expected_address == real_address.decode('utf-8')
