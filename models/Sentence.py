from pydantic import BaseModel

class Sentence(BaseModel):
    troyka_id: int
    description: str
    ifExecution: bool