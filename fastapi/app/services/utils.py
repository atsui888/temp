import os
from dotenv import load_dotenv
from upstash_redis import Redis
from app.models.Polls import Poll

load_dotenv()
REDIS_REST_API_URL = os.getenv('KV_REST_API_URL')
REDIS_REST_API_TOKEN = os.getenv('KV_REST_API_TOKEN')
redis_client = Redis(url=REDIS_REST_API_URL, token=REDIS_REST_API_TOKEN)


def save_poll(poll: Poll):
    redis_client.set(f"poll: {poll.id}", poll.model_dump_json())

