import string
import secrets
from sqlalchemy.orm import Session
from models.models import Shortener

class URLShortenerService:
    def __init__(self, url, db):
        self.url = url
        self.unique_key = None
        self.shorten_url = None
        self.base_url = 'tier.app'
        self.db = db

    def get_db_url_by_key(self, key) -> Shortener:
        return (
            self.db.query(Shortener)
            .filter(Shortener.unique_key == key)
            .first()
        )

    def generate_random_identifier(self):
        ''' Generate Short Unique Identifier'''

        key = None
        characters = string.ascii_letters + string.digits

        while True:
            key = ''.join(secrets.choice(characters) for i in range(10))
            if (any(c.islower() for c in key)
                    and any(c.isupper() for c in key)
                    and sum(c.isdigit() for c in key) >= 3):
                break
        return key


    def generate_unique_random_identifier(self) -> str:
        key = self.generate_random_identifier()
        while self.get_db_url_by_key(key):
            key = self.generate_random_identifier()
        return key

    def create_db_url(self) -> Shortener:
        db_url = Shortener(
            original_url=self.url, shorten_url=self.shorten_url, unique_key=self.unique_key
        )
        self.db.add(db_url)
        self.db.commit()
        self.db.refresh(db_url)
        return db_url

        
    def shorten_url_obj(self):
        self.unique_key = self.generate_unique_random_identifier()
        self.shorten_url = self.base_url + '/' + self.unique_key
        insert_obj_to_db = self.create_db_url()
        print(insert_obj_to_db)
        return insert_obj_to_db
        

