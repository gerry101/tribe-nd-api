from fastapi import APIRouter
from models.post import Post
from config.db import db
from bson import ObjectId
from schemas.main import serializeDict, serializeList

post = APIRouter()


@post.post('/post')
async def create_post(post: Post):
    db.post.insert_one(dict(post))
    inserted_post = db.post.find_one(
        {"title": post.title, "timePosted": post.timePosted})
    return serializeDict(inserted_post)


@post.get("/post")
async def get_all_posts():
    return serializeList(db.post.find())


@post.get("/post/{id}")
async def find_a_single_post(id):
    print("Finding single post")
    found_post = db.post.find_one({"_id": ObjectId(id)})
    if found_post:
        return serializeDict(found_post)
    else:
        return {
            "error": "Post not found"
        }
