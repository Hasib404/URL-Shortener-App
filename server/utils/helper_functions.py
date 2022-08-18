import re
import string
import secrets
from sqlalchemy.orm import Session
from db import crud

def is_valid_url(url):
    ''' Regex to check if URL is valid '''

    pattern = ("((http|https)://)(www.)?" +
            "[a-zA-Z0-9@:%._\\+~#?&//=]" +
            "{2,256}\\.[a-z]" +
            "{2,6}\\b([-a-zA-Z0-9@:%" +
            "._\\+~#?&//=]*)")
    
    regex_compiler = re.compile(pattern)

    if (url == None):
        return False

    if(re.search(regex_compiler, url)):
        return True
    else:
        return False

def generate_random_identifier():
    ''' Generate SHort Unique Identifier'''

    characters = string.ascii_letters + string.digits
    unique_key = None

    while True:
        unique_key = ''.join(secrets.choice(characters) for i in range(10))
        if (any(c.islower() for c in unique_key)
                and any(c.isupper() for c in unique_key)
                and sum(c.isdigit() for c in unique_key) >= 3):
            break
    return unique_key


def generate_unique_random_identifier(db: Session) -> str:
    key = generate_random_identifier()
    while crud.get_db_url_by_key(db, key):
        key = generate_random_identifier()
    return key