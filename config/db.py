import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

CONN_URL = os.environ.get("MONGODB_CONN")
DB_NAME = os.environ.get("DB_NAME")

conn = MongoClient(os.environ.get("MONGODB_CONN"), tlsCAFile=certifi.where())
db = conn[DB_NAME]
