import os
from dotenv import load_dotenv
from upstash_redis import Redis
from app.models.Polls import Poll
from uuid import UUID
from typing import Optional

load_dotenv()
REDIS_REST_API_URL = os.getenv('KV_REST_API_URL')
REDIS_REST_API_TOKEN = os.getenv('KV_REST_API_TOKEN')
redis_client = Redis(url=REDIS_REST_API_URL, token=REDIS_REST_API_TOKEN)


def save_poll(poll: Poll):
    poll_json = poll.model_dump_json()
    redis_client.set(f"poll_{poll.id}", poll_json)


def get_poll(poll_id: UUID) -> Optional[Poll]:
    poll_json = redis_client.get(f"poll_{poll_id}")

    print(f"poll_json: {type(poll_json)} *** \n{poll_json} \n*******")

    if poll_json:

        return Poll.model_validate_json(poll_json)
    else:
        return None
