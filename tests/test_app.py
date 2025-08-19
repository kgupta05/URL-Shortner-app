import pytest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_get(client):
    """Test that GET request to / returns status 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_url_shortening(client):
    """Test that POST request creates a shortened URL"""
    response = client.post("/", data={"long_url": "https://example.com"})
    assert response.status_code == 200
    assert b"Shortened URL:" in response.data
