import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from faker import Faker

from config import MONGO_URI

fake = Faker()
client = AsyncIOMotorClient(MONGO_URI)
db = client["glossary"]

async def seed():
    terms = []
    for _ in range(2000):
        terms.append({
            "title": fake.word(),
            "description": fake.sentence(),
            "tags": fake.words(3)
        })

    await db.terms.insert_many(terms)
    print("Data seeded")

asyncio.run(seed())
