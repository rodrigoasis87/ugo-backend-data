from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField
from typing import Optional


class Experience(BaseModel):
    name: str = Field(...)
    type: str = Field(...)
    description: str = Field(...)
    country: str = Field(...)
    province: str = Field(...)
    price_min: int = Field(...)
    price_max: int = Field(...)


class ExperienceResponse(BaseModel):
    id: ObjectIdField = Field(..., alias="_id")
    name: str = Field(...)
    type: str = Field(...)
    description: str = Field(...)
    country: str = Field(...)
    province: str = Field(...)
    price_min: int = Field(...)
    price_max: int = Field(...)


class ExperienceUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]


class Review(BaseModel):
    exp_id: ObjectIdField = Field(...)
    calification: int = Field(...)
    comment: str = Field(...)


class ReviewResponse(BaseModel):
    exp_id: ObjectIdField = Field(...)
    calification: int = Field(...)
    comment: str = Field(...)
