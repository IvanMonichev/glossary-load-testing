from faker import Faker
from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_URI

fake = Faker()
client = AsyncIOMotorClient(MONGO_URI)
db = client["glossary"]

fake = Faker()

client = AsyncIOMotorClient(MONGO_URI)
db = client["glossary"]

async def seed_if_needed():
    count = await db.terms.count_documents({})

    if count > 0:
        print(f"Seed skipped — already have {count} documents")
        return

    print("Seeding database...")
    terms = []

    for _ in range(2000):
        terms.append({
            "title": fake.word(),
            "description": fake.sentence(),
            "tags": fake.words(3)
        })

    await db.terms.insert_many(terms)
    print("Seed completed.")
