from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_products_by_category():
    response = client.get("/products?category=snacks")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 2,
            "name": "Lays",
            "category": "snacks",
        }
    ]


def test_get_product():
    response = client.get("/products/2")

    assert response.status_code == 200
    assert response.json()["name"] == "Lays"


def test_create_product():
    response = client.post(
        "/products",
        json={
            "name": "Snickers",
            "category": "sweets",
        },
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Snickers"
    assert response.json()["category"] == "sweets"