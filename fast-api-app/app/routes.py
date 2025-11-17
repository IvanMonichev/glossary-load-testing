from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.db import terms_collection
from app.schemas import TermOut

router = APIRouter()

@router.get("/terms/{term_id}", response_model=TermOut)
async def get_term(term_id: str):
    term = await terms_collection.find_one({"_id": ObjectId(term_id)})
    if not term:
        raise HTTPException(404, "Term not found")

    return {
        "id": str(term["_id"]),
        "title": term["title"],
        "description": term["description"],
        "tags": term["tags"],
    }


@router.get("/terms", response_model=list[TermOut])
async def search_terms(query: str = "", page: int = 1, page_size: int = 20):
    skip = (page - 1) * page_size

    cursor = terms_collection.find(
        {"title": {"$regex": query, "$options": "i"}}
    ).skip(skip).limit(page_size)

    results = []
    async for term in cursor:
        results.append({
            "id": str(term["_id"]),
            "title": term["title"],
            "description": term["description"],
            "tags": term["tags"],
        })

    return results
