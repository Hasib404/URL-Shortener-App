from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from db.database import Database
from main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    database = Database()
    engine = database.get_db_connection()
    session = database.get_db_session(engine)
    yield session


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c