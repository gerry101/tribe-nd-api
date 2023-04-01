from fastapi import APIRouter
from models.dtr import DTR
from config.db import db
from bson import ObjectId
from schemas.main import serializeDict

dtr = APIRouter()


@dtr.post("/dtr")
async def dtr_handler(dtr: DTR):
    if not dtr.verified:
        db.dtr.insert_one(dict(dtr))
    new_score = len(dtr.reviews) + dtr.ratings + \
        len(dtr.comments) - dtr.infractions
    dtr.currentScore = new_score
    db.dtr.insert_one(dict(dtr))
    return serializeDict(dtr)
