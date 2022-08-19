from typing import Dict, Generator
from main import app
from models import response
import pytest
from fastapi.testclient import TestClient

from server.db.config import SessionLocal
from main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as test_client:
        yield test_client