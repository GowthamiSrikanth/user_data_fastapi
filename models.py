from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int
    city: str
    created_at: date
