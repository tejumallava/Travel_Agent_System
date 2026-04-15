from pydantic import BaseModel

class TravelRequest(BaseModel):
    origin: str
    destination: str
    date: str
    travelers: int = 1
    budget: float = None