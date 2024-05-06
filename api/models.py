from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField
from typing import Optional

NOT_FOUND_IMAGE = "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1200,h=630,fit=crop,f=jpeg/mk3Ew9MwlbcqZJba/img-YbNxzkRwGaHlxOXV.jpg"


class Experience(BaseModel):
    name: str = Field(...)
    type: str = Field(...)
    description: str = Field(...)
    country: str = Field(...)
    province: str = Field(...)
    price_min: int = Field(...)
    price_max: int = Field(...)
    discount: int = Field(0)
    imageUrl: str = Field(NOT_FOUND_IMAGE)


class ExperienceResponse(BaseModel):
    id: ObjectIdField = Field(..., alias="_id")
    name: str = Field(...)
    type: str = Field(...)
    description: str = Field(...)
    country: str = Field(...)
    province: str = Field(...)
    price_min: int = Field(...)
    price_max: int = Field(...)
    discount: int = Field(0)
    imageUrl: str = Field(NOT_FOUND_IMAGE)


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
