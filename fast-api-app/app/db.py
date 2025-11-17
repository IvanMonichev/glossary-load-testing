from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import MONGO_URI

load_dotenv()

DB_NAME = "glossary"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
terms_collection = db.get_collection("terms")