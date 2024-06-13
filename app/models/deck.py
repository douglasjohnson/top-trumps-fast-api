from typing import List, Optional

from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId


class Attribute(BaseModel):
    type: str = Field(...)
    value: int = Field(..., ge=0)


class Card(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    imageUrl: str = Field(...)
    attributes: List[Attribute] = Field(...)


class AttributeType(BaseModel):
    name: str = Field(...)
    units: str = Field(...)


class Deck(BaseModel):
    id: Optional[PydanticObjectId] = None
    name: str = Field(...)
    imageUrl: str = Field(...)
    cards: List[Card] = Field(...)
    attributes: List[AttributeType] = Field(...)
