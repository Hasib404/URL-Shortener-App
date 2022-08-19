from utils.helper_functions import is_valid_url
from services.shortener_service import URLShortenerService
from main import app
from tests.conftest import db, client



def test_is_valid_url() -> None:
    new_product = "http://google.com"
    response = is_valid_url(new_product)
    assert response

def test_is_not_valid_url() -> None:
    new_product = "http:/google.com"
    response = is_valid_url(new_product)
    assert not response

def test_random_identifier_length(db) -> None:
    url = "http://google.com"
    shrtener_service = URLShortenerService(url, db)

    response = shrtener_service.generate_random_identifier()
    key_length = len(response)
    assert key_length == 10

def test_unique_identifier(db) -> None:
    url = "http://google.com"
    shrtener_service = URLShortenerService(url, db)

    response = shrtener_service.generate_unique_random_identifier()
    key_length = len(response)
    assert key_length == 10

def test_shorten_url_obj(db) -> None:
    url = "http://google.com"
    shrtener_service = URLShortenerService(url, db)

    response = shrtener_service.shorten_url_obj()
    # key_length = len(response)
    # assert key_length == 10


# def test_is_valid_url(client: TestClient, db: Session) -> None:
#     new_product = {
#         "name": "Iphone",
#         "price": 750,
#         "is_available": True
#     }
#     response = client.post("products/add", json=new_product)

#     content = response.json()
#     assert response.status_code == 200
#     assert content["message"] == "Product added successfully."