from pydantic import BaseModel
from datetime import datetime


class Post(BaseModel):
    timePosted: datetime = datetime.now()
    sellingPrice: float
    sellerFirstName: str
    sellerLastName: str
    title: str
    description: str
    negotiable: bool
    available: bool
    numComments: int
