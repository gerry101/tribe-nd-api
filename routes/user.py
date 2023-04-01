from fastapi import APIRouter
from models.user import User
from config.db import db
from bson import ObjectId
from schemas.user import userEntity, usersEntity

user = APIRouter()


@user.post('/signup')
async def sign_up(user: User):
    db.user.insert_one(dict(user))
    inserted_user = db.user.find_one({"email": user.email})
    return userEntity(inserted_user)


@user.post('/login')
async def login(user: User):
    found_user = db.user.find_one(
        {"email": user.email, "password": user.password})
    if found_user:
        return userEntity(found_user)
    return {
        "error": "User not found"
    }


@user.put("/{id}")
async def update_user(id, user: User):
    db.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return userEntity(db.user.find_one({"_id": ObjectId(id)}))


@user.delete("/{id}")
async def delete_user(id, user: User):
    return userEntity(db.user.find_one_and_delete({"_id": ObjectId(id)}))


@user.get('/user/{id}')
async def find_a_single_user(id):
    return userEntity(db.user.find_one({"_id": ObjectId(id)}))


@user.get('/user')
async def find_all_users():
    print("II")
    return usersEntity(db.user.find())
