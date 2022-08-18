from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, BIGINT, String, TIMESTAMP, BOOLEAN, text

Base = declarative_base()

class Product(Base):
    __tablename__ = "product"
    id = Column(INTEGER, primary_key=True)
    name = Column(String(1024), nullable=False)
    price = Column(BIGINT)
    is_available = (Column(BOOLEAN, default=True))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))