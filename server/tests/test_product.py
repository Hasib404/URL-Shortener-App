from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def test_add_new_product(client: TestClient, db: Session) -> None:
    new_product = {
        "name": "Iphone",
        "price": 750,
        "is_available": True
    }
    response = client.post("products/add", json=new_product)

    content = response.json()
    assert response.status_code == 200
    assert content["message"] == "Product added successfully."

