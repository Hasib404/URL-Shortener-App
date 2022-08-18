from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text

Base = declarative_base()

class Shortener(Base):
    __tablename__ = "shortener"
    id = Column(Integer, primary_key=True)
    original_url = Column(String(1024), nullable=False)
    unique_key = Column(String, unique=True, index=True)
    shorten_url = Column(String(1024), nullable=False)
    clicks = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))