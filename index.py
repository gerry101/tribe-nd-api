from fastapi import FastAPI
from routes.user import user
from routes.post import post
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(post)
