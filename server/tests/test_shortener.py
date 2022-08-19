from utils.helper_functions import is_valid_url
from services.shortener_service import URLShortenerService
import json


def test_is_valid_url() -> None:
    '''Test validity of the URL'''
    new_product = "http://google.com"
    response = is_valid_url(new_product)
    assert response

def test_is_not_valid_url() -> None:
    '''Test not valid URL'''
    new_product = "http:/google.com"
    response = is_valid_url(new_product)
    assert not response

def test_random_identifier_length(db) -> None:
    '''Test random identifier'''
    url = "http://google.com"
    shrtener_service = URLShortenerService(url, db)

    response = shrtener_service.generate_random_identifier()
    key_length = len(response)
    assert key_length == 10

def test_unique_identifier(db) -> None:
    '''Test unique random identifier'''
    url = "http://google.com"
    shrtener_service = URLShortenerService(url, db)

    response = shrtener_service.generate_unique_random_identifier()
    key_length = len(response)
    assert key_length == 10

def test_valid_shorten_url_obj(client) -> None:
    '''Test validity of the genearted object'''
    url = {
            "url": "http://abc.com"
        }
    response = client.post("/url", data=json.dumps(url))
    content = response.json()
    assert content["code"] == 200
    assert len(content["data"]["shortener_id"]) > 0
    assert content["message"] == "shortener object added successfully."
    assert content["error"] == False

def test_not_valid_shorten_url(client) -> None:
    '''Test Error of the genearted object'''
    url = {
            "url": "http:/abc.com"
        }
    response = client.post("/url", data=json.dumps(url))
    content = response.json()
    assert content["code"] == 400
    assert len(content["data"]) == 0
    assert content["message"] == "Invalid URL"
    assert content["error"] == True
