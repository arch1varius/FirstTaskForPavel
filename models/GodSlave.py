from pydantic import BaseModel
from typing import Literal, Optional


class RabOfGod(BaseModel):
    login: str
    password: str
    position: Literal['Чекист', 'Член ВКП(б)', 'Прокурор', 'Простой смертный']
    fullname: str
    photo_URL: Optional[str] = None
    ifTrockist: bool
