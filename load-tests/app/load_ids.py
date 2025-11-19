from pymongo import MongoClient
import os


def load_term_ids():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://admin:password@mongo:27017/?authSource=admin")
    client = MongoClient(mongo_uri)
    db = client["glossary"]

    # Берём первые N id
    cursor = db.terms.find({}, {"_id": 1}).limit(100)

    ids = [str(doc["_id"]) for doc in cursor]
    print(f"Loaded {len(ids)} term ids")
    return ids
