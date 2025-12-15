from pydantic import BaseModel

class Team_Pokemon(BaseModel):
    name: str
    captain: str
