from fastapi import APIRouter
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.responses import FileResponse, RedirectResponse
from models.GodSlave import RabOfGod
from models.Troyka import Troyka
from models.Login_Data import Login_Data
from models.Sentence import Sentence
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from DataBase.DBDeclaration import GodSlaveModel, TroykaModel, SentenceModel
from fastapi.security import OAuth2PasswordRequestForm
from auth.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)
from deps import get_current_user

router = APIRouter()


@router.post("/troyka")
def addTroyka(troyka: Troyka):
    troykaModel = TroykaModel(name = troyka.name, gebist_id = troyka.gebist_id,
                               commy_id = troyka.commy_id, prokuror_id = troyka.prokuror_id)
    db.add(troykaModel)
    db.commit()
    return {"message": troyka}


@router.get("/troyka/{id}")
def getTroykaByID(id: int):
    troyka = db.get(TroykaModel, id)
    return {"RabOfGod": troyka}


@router.get("/troyka")
def getTroykas():
    troykas = db.query(TroykaModel).all()
    return {"RabOfGod[]": troykas}