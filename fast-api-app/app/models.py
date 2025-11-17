from pydantic import BaseModel


class Term(BaseModel):
    id: str
    title: str
    description: str
    tags: list[str]