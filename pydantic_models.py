from pydantic import BaseModel
from typing import List, Optional

class Id(BaseModel):
    id: int

class Text(BaseModel):
    text: str

class Size(BaseModel):
    url: str

class Photo(BaseModel):
    sizes: List[Size]

class Attachment(BaseModel):
    photo: Photo

class Item(BaseModel):
    id: int
    text: str
    is_pinned: Optional[int] = None
    attachments: List[Attachment]

class Items(BaseModel):
    items: List[Item]


