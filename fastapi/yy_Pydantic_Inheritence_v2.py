from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

class VoterBase(BaseModel):
    email: EmailStr
    voted_at: Optional[datetime] = Field(default_factory=datetime.now)


class CCKVoter(VoterBase):
    # actually this class could have been combined with VoterBase, but I wanted to test how Pydantic model
    # inherited from another pydantic model
    town: str = "CCK"
    postal_code: str = '123321'


class AMKVoter(VoterBase):
    # actually this class could have been combined with VoterBase, but I wanted to test how Pydantic model
    # inherited from another pydantic model
    town: str = "AMK"
    postal_code: str = '987789'


if __name__ == "__main__":
    voters = [
        CCKVoter(email="111@cck.com"),
        CCKVoter(email="222@cck.com"),
        AMKVoter(email="333@amk.com")
    ]
    for v in voters:
        print(v.town, v.email, v.voted_at, v.postal_code)

    pass