from pydantic import BaseModel
from typing import Literal


class RabOfGod(BaseModel):
    login: str
    password: str
    position: Literal['Чекист', 'Член ВКП(б)', 'Прокурор', 'Простой смертный']
    fullname: str
    photo_URL: str | None = None
    ifTrockist: bool
