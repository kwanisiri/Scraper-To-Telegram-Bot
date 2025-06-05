from pydantic import BaseModel

class Lead(BaseModel):
    name: str
    url: str
    score: float