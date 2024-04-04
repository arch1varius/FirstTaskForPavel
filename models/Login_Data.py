from pydantic import BaseModel


class Login_Data(BaseModel):
    login: str
    password: str