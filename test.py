import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_add_numbers(client):
    response = client.get('/add/3/4')
    assert response.status_code == 200
    assert response.json['result'] == 7