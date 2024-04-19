from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField
from typing import Optional


class Experience(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    type: str = Field(...)


class ExperienceResponse(BaseModel):
    id: ObjectIdField = Field(..., alias="_id")
    name: str = Field(...)
    description: str = Field(...)


class ExperienceUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]


class Review(BaseModel):
    title: str = Field(...)
    opinion: str = Field(...)


class ReviewResponse(BaseModel):
    id: str = Field(..., )
    exp_id: str = Field(...)
    title: str = Field(...)
    opinion: str = Field(...)
