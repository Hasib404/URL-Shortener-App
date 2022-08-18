from sqlalchemy.orm import Session
from utils.helper_functions import generate_unique_random_identifier
from models.request import URLOrigin
from models.models import Shortener
from services.shortener_service import URLShortenerService


def create_db_url(db: Session, url_origin: URLOrigin) -> Shortener:
    key = generate_unique_random_identifier(db)
    shortener_service = URLShortenerService(url_origin.url, key)
    shorten_url = shortener_service.shorten_url()
    db_url = Shortener(
        original_url=url_origin.url, shorten_url=shorten_url, unique_key=key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_db_url_by_key(db: Session, url_key: str) -> Shortener:
    return (
        db.query(Shortener)
        .filter(Shortener.unique_key == url_key)
        .first()
    )