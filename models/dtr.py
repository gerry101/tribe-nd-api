from pydantic import BaseModel
from datetime import datetime


class DTR(BaseModel):
    ratings: int
    reviews: list
    comments: list
    infractions: int
    currentScore: int = 0
    verified: bool = False
