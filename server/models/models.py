from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from db.config import Base


class Shortener(Base):
    __tablename__ = "shortener"
    id = Column(Integer, primary_key=True)
    original_url = Column(String(1024), nullable=False)
    unique_key = Column(String, unique=True, index=True)
    shorten_url = Column(String(1024), nullable=False)
    created_at = Column(
        TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )


class URLClicks(Base):
    __tablename__ = "visits"
    id = Column(Integer, primary_key=True)
    visited_url_key = Column(String(1024), nullable=False)
    clicks = Column(Integer, default=0)
