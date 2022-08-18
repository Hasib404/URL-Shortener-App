from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class URLOrigin(BaseModel):
    url: str = Field(
        None, title="Long URL", max_length=1000
    )

class URLShorten(URLOrigin):
    clicks: int = Field(
        None, title="Times clicked"
    )
    class Config:
        orm_mode = True

