import os
from dotenv import load_dotenv
import redis
import pymongo
import asyncio
import json

load_dotenv()

# Redis configuration
redis_client = redis.Redis(host='localhost', port=6379, db=0)



# MongoDB configuration
mongodb_uri = os.getenv("MONGODB_URI")
mongodb_database = os.getenv("MONGODB_DATABASE")
if mongodb_database is None:
    raise ValueError("MONGODB_DATABASE environment variable not set")
mongo_client = pymongo.MongoClient(mongodb_uri)
db = mongo_client[mongodb_database]
sessions_collection = db["sessions"]

async def cache_result(key: str, result: dict, ttl: int = 3600) -> None:
    try:
        redis_client.set(key, json.dumps(result), ex=ttl)
    except Exception as e:
        print(f"Redis error: {e}")

async def get_cached_result(key: str) -> dict:
    try:
        cached_result = redis_client.get(key)
        if cached_result:
            return json.loads(cached_result)
        return None
    except Exception as e:
        print(f"Redis error: {e}")
        return None

async def save_session_data(session_id: str, data: dict):
    sessions_collection.update_one({"session_id": session_id}, {"$set": data}, upsert=True)

async def get_session_data(session_id: str):
    session_data = sessions_collection.find_one({"session_id": session_id})
    return session_data
