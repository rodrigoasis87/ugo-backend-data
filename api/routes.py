from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic_mongo import ObjectIdField
from typing import List
from api.models import Experience, ExperienceResponse, ExperienceUpdate

router = APIRouter()

HTTP_404 = status.HTTP_404_NOT_FOUND
MSG_404 = "Experience not found"

# GET /experience : Returns all experiences


@router.get("/", response_description="List all experiences", response_model=List[ExperienceResponse])
def list_experiences(request: Request, category: str | None = None):
    query = {"type": category} if category else {}
    return list(request.app.database["experiences"].find(query, limit=100))


# POST /experience : Creates a new experience


@router.post("/", response_description="Create a new experience", status_code=status.HTTP_201_CREATED, response_model=Experience)
def create_experience(request: Request, experience: Experience = Body(...)):
    item_dict = experience.model_dump()
    item = request.app.database["experiences"].insert_one(item_dict)
    item_dict["_id"] = str(item.inserted_id)
    return JSONResponse(content=item_dict, status_code=201)


# GET /experience/{id} : Returns the details of a given experience


@router.get("/{id}", response_description="Get a single experience by id", response_model=Experience)
def find_experience(id: str, request: Request):
    if (exp := request.app.database["experiences"].find_one({"_id": ObjectIdField(id)})) is not None:
        return exp
    raise HTTPException(status_code=HTTP_404, detail=MSG_404)


# PUT /experience/{id} : Updates a given experience


@router.put("/{id}", response_description="Update a experience", response_model=Experience)
def update_experience(id: str, request: Request, experience: ExperienceUpdate = Body(...)):
    items = experience.model_dump().items()
    experience = {k: v for k, v in items if v is not None}
    if len(experience) >= 1:
        update_result = request.app.database["experiences"].update_one(
            {"_id": ObjectIdField(id)}, {"$set": experience})

        if update_result.modified_count == 0:
            raise HTTPException(status_code=HTTP_404, detail=MSG_404)

    if (existing_experience := request.app.database["experiences"].find_one({"_id": ObjectIdField(id)})) is not None:
        return existing_experience

    raise HTTPException(status_code=HTTP_404, detail=MSG_404)


# DELETE /experience/{id} : Deletes a given experience


@router.delete("/{id}", response_description="Delete a experience")
def delete_experience(id: str, request: Request, response: Response):
    delete_result = request.app.database["experiences"].delete_one(
        {"_id": ObjectIdField(id)})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=HTTP_404, detail=MSG_404)
