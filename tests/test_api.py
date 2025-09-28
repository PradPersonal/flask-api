import pytest
from app import app as flask_app  # Assuming your Flask app instance is named 'app' in app.py
import json

@pytest.fixture
def client():
    """A test client for the app."""
    # Set Flask to testing mode
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert json.loads(response.data) == {'message': 'Hello, Flask API!'}

def test_get_all_items(client):
    """Test the endpoint to get all items."""
    response = client.get('/items')
    assert response.status_code == 200
    expected_items = [
        {"id": 1, "name": "Apple"},
        {"id": 2, "name": "Banana"},
        {"id": 3, "name": "Cherry"}
    ]
    assert json.loads(response.data) == expected_items

def test_get_single_item(client):
    """Test the endpoint to get a single item by ID."""
    response = client.get('/items/2')
    assert response.status_code == 200
    expected_item = {"id": 2, "name": "Banana"}
    assert json.loads(response.data) == expected_item

def test_get_non_existent_item(client):
    """Test for an item that does not exist."""
    response = client.get('/items/99')
    assert response.status_code == 404
    assert json.loads(response.data) == {'error': 'Item not found'}

def test_create_new_item(client):
    """Test the endpoint to create a new item."""
    new_item_data = json.dumps({"name": "Grapes"})
    response = client.post('/items', data=new_item_data, content_type='application/json')
    assert response.status_code == 201
    assert json.loads(response.data) == {"id": 4, "name": "Grapes"}
