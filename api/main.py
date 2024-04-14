import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pymongo import MongoClient
from api.routes import router as experience_router

load_dotenv(override=True)

database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")
database_url = os.getenv("DATABASE_URL")
database_name = os.getenv("DATABASE_NAME")

connection_string = f"mongodb+srv://{database_user}:{database_password}@{database_url}"

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(connection_string)
    app.database = app.mongodb_client[database_name]


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(
    experience_router,
    tags=["experiences"],
    prefix="/experience"
)
