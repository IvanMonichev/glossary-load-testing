from pydantic import BaseModel

class TermSchema(BaseModel):
    title: str
    description: str
    tags: list[str]

class TermOut(TermSchema):
    id: str
