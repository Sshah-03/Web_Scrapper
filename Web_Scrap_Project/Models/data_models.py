from pydantic import BaseModel, HttpUrl
from typing import Optional

class NewsItem(BaseModel):
    source: str
    title: str
    url: Optional[HttpUrl]
    score: Optional[int] = None
