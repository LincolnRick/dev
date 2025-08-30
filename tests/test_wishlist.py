import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_wishlist_flow():
    user_id = 1
    item = {
        "card_id": "abc123",
        "name": "Sample Card",
        "set_name": "Base Set",
    }
    response = client.post(f"/users/{user_id}/wishlist/", json=item)
    assert response.status_code == 201
    response = client.get(f"/users/{user_id}/wishlist/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    response = client.delete(f"/users/{user_id}/wishlist/", params={"card_id": "abc123"})
    assert response.status_code == 204
    response = client.get(f"/users/{user_id}/wishlist/")
    assert response.status_code == 200
    assert response.json() == []
