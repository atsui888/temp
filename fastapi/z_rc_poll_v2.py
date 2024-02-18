from datetime import datetime, timezone
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Union
from uuid import UUID, uuid4
from fastapi import HTTPException


class Choice(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    label: int = Field(gt=0, lt=6)
    description: str = Field(min_length=1, max_length=100)


class Poll(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(min_length=5, max_length=50)
    options: List[Choice]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: Optional[datetime] = None

    @field_validator("options", mode="before")  # ignore this pycharm error
    @classmethod
    def validate_options(cls, v: List[str]) -> List[Choice]:
        # rc: Pydantic does not appear to check if v is a list if the mode="before", so I need to check it myself
        if not isinstance(v, list):
            raise HTTPException(
                status_code=400,
                detail="Choice must be a 'List of Str'."
            )
        if len(v) < 2 or len(v) > 5:
            raise HTTPException(
                status_code=400,  # 400 == bad request
                detail="A poll must contain between 2 and 5 choices."
            )

        vc = [Choice(label=idx+1, description=choice_text) for idx, choice_text in enumerate(v)]
        return vc


if __name__ == "__main__":
    # p1 = Poll(title="Poll 1", options=["Yes", "No", "Maybe"])
    p1 = Poll(title="Poll 1", options={"a": 1, "b": 2})
    print(p1.id, p1.title, p1.created_at, p1.expires_at)
    # print(type(p1.options))
    for c in p1.options:
        # print(c.id, c.label, c.description)
        print(c.model_dump_json())

