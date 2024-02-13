# https://www.udemy.com/course/pydantic-advanced-data-validation/
# $> uvicorn main:app --reload
# vercel.com (for redis on cloud usage)
# pip install upstash-redis

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from upstash_redis import Redis
from app.models.Polls import Poll, PollCreate
from app.services import utils
from uuid import UUID


load_dotenv()  # set environment variables from .env.
REDIS_REST_API_URL = os.getenv('KV_REST_API_URL')
REDIS_REST_API_TOKEN = os.getenv('KV_REST_API_TOKEN')

app = FastAPI()


@app.get("/test")
def test():
    return {"message": "hello there"}


@app.post("/polls/create")
def create_poll(poll: PollCreate):
    # rc: seems like easier to understand if "poll: PollCreate" to "pc: PollCreate"
    # then poll = pc.create_poll()
    # but actually, I am uncomfortable with this code from the authors, it would seem that
    # poll = Poll(attributes) is more pythonic and understandable where the new poll is created from __init__
    # rather than using a extra object "PollCreate" to create a "Poll" object. If the reason for this way of doing
    # things is to save on code lines, then maybe using composition is better ??
    new_poll = poll.create_poll()
    utils.save_poll(new_poll)
    return {
        "detail": "Poll successfully created.",
        "poll_id": new_poll.id,
        "poll": new_poll
    }


@app.get("/polls/{poll_id}")
def get_poll(poll_id: UUID):
    poll = utils.get_poll(poll_id)
    if not poll:
        raise HTTPException(
            status_code=404,
            detail=f"A poll with id: '{poll_id}' is not found.")
    else:
        return poll


# exploration code - to be deleted later
redis_client = Redis(url=REDIS_REST_API_URL, token=REDIS_REST_API_TOKEN)


@app.post("/redis/save", tags=["throwaway"])
def save_redis(uid: str, name: str):
    redis_client.set(uid, name)
    return {"status": "success"}


@app.get("/redis/get/{uid}")
def get_redis(uid: str):
    return {"uid": uid, "name": redis_client.get(uid)}
