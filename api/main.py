from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde .env y sobrescribe con cualquier variable de .env.local si existe
load_dotenv(override=True)  # Asegúrate de poner `override=True` para permitir sobrescribir con .env.local

# Uso de las variables de entorno
database_url = os.getenv("DATABASE_URL")
database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")

uri = f"mongodb+srv://{database_user}:{database_password}@{database_url}"
client = MongoClient(uri)
db = client["sample_mflix"]
collection = db["comments"]

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.post("/items/")
async def create_item(item: Item):
    collection.insert_one(item.model_dump())
    return item

@app.get("/items/")
async def read_items():
    items = list(collection.find({}, { "_id": 0, "name": 1, "email": 1, "text": 1 }))
    return items

@app.delete("/items/")
async def delete_all_items():
    collection.delete_many({})
    return "Done"

@app.get("/")
async def server_up():
    return "Server UP and running..."