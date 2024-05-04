from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic_mongo import ObjectIdField
from typing import List
from api.models import Review, ReviewResponse

router = APIRouter()

HTTP_404 = status.HTTP_404_NOT_FOUND
MSG_404 = "Experience not found"


# GET /experience/{id}/review

@router.get("/{id}/review", response_description="Returns all reviews for a given experience", response_model=List[Review])
def return_reviews(id: str, request: Request):
    id = ObjectIdField(id)
    reviews = request.app.database["reviews"].find({"exp_id": id})
    if reviews is not None:
        return list(reviews)
    raise HTTPException(status_code=HTTP_404, detail=MSG_404)


# POST /experience/{id}/review

@router.post("/{id}/review", response_description="Create a new experience review", status_code=status.HTTP_201_CREATED, response_model=ReviewResponse)
def create_review(id: str, request: Request, review: Review = Body(...)):
    item_dict = review.model_dump()
    item_dict["exp_id"] = ObjectIdField(id)
    item = request.app.database["reviews"].insert_one(item_dict)
    item_dict["exp_id"] = id
    item_dict["_id"] = str(item.inserted_id)
    print(item_dict)
    return JSONResponse(content=item_dict, status_code=201)
