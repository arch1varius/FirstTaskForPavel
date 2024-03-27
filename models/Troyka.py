from pydantic import BaseModel


class Troyka(BaseModel):
    name: str
    gebist_id: int
    commy_id: int
    prokuror_id: int
