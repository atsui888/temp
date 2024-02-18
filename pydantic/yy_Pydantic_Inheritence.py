from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional


class VoterBase(BaseModel):
    voted_at: Optional[datetime] = Field(default_factory=datetime.now)


class CCKVoter(VoterBase):
    # actually this class could have been combined with VoterBase, but I wanted to test how Pydantic model
    # inherited from another pydantic model
    town: str = "CCK"
    email: EmailStr


class VoterFactory:
    def __init__(self, town: str, email: EmailStr):
        if town == "CCK":
            self.voter = CCKVoter(email=email)



if __name__ == "__main__":
    cck_voters = [
        VoterFactory(town="CCK", email="aaa@bbb.com"),
        VoterFactory(town="CCK", email="222@333.com")
    ]

    print()
    for cck in cck_voters:
        print(cck.voter.town, cck.voter.email, cck.voter.voted_at)

    pass
