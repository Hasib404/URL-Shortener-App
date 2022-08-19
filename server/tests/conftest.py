from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from server.db.config import SessionLocal
from main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c