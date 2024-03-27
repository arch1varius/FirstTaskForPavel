from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.responses import FileResponse, RedirectResponse
from models.GodSlave import RabOfGod
from models.Troyka import Troyka
from models.Sentence import Sentence
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from DataBase.DBDeclaration import GodSlaveModel, TroykaModel, SentenceModel
from auth.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)

SQLALCHEMY_DATABASE_URL = "sqlite:///./DataBase/sql_troyki.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

def login_user(login : str, password: str):
    user = db.query(GodSlaveModel).filter(GodSlaveModel.login == login).first()
    print(user.login, user.password)
login_user("pavel1937", "gfdgdf")