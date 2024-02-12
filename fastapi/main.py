# https://www.udemy.com/course/pydantic-advanced-data-validation/
# $> uvicorn main:app --reload

from fastapi import FastAPI
from app.models.Polls import Poll, PollCreate

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
    return {
        "detail": "Poll successfully created.",
        "poll_id": new_poll.id
    }
