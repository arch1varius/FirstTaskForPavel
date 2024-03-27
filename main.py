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

app = FastAPI()
@app.post("/signup")
async def signup_user(user: RabOfGod):
    user_in_db = db.query(GodSlaveModel).filter(GodSlaveModel.login == user.email).first()
    if user_in_db is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this login already exist"
        )
    slaveModel = GodSlaveModel(login=user.login, password=user.password,
                               position = user.position, fullname = user.fullname,
                               photo_URL = user.photo_URL, ifTrockist = user.ifTrockist)

    db.add(slaveModel)
    db.commit()
    return {"message": slaveModel}

@app.post("/login")
async def login_user(login : str, password: str):
    user = db.query(GodSlaveModel).filter(GodSlaveModel.login == login).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    hashed_passwd = user.password
    if not verify_password(password, hashed_passwd):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    return {
        "access_token": create_access_token(user.login),
        "refresh_token": create_refresh_token(user.login),
    }


# @app.post("/slave")
# def addSlave(slave: RabOfGod):
#     slaveModel = GodSlaveModel(login = slave.login, password = slave.password,
#                                position = slave.position, fullname = slave.fullname,
#                                photo_URL = slave.photo_URL, ifTrockist = slave.ifTrockist)
#     db.add(slaveModel)
#     db.commit()
#     return {"message": slaveModel}
# @app.get("/slave/{id}")
# def getSlaveByID(id: int):
#     slaveModel = db.get(GodSlaveModel, id)
#     return {"RabOfGod": slaveModel}
# @app.get("/slave")
# def getSlaves():
#     slaves = db.query(GodSlaveModel).all()
#     return {"RabOfGod[]": slaves}
@app.patch("/slave/{id}")
def patchSlaveByID(id: int, slave: RabOfGod):
    slaveModel = db.get(GodSlaveModel, id)
    slaveModel.login = slave.login
    slaveModel.password = slave.password
    slaveModel.position = slave.position
    slaveModel.fullname = slave.fullname
    slaveModel.photo_URL = slave.photo_URL
    slaveModel.ifTrockist = slave.ifTrockist
    db.commit()
    return {"RabOfGod": slave}

@app.post("/troyka")
def addTroyka(troyka: Troyka):
    troykaModel = TroykaModel(name = troyka.name, gebist_id = troyka.gebist_id,
                               commy_id = troyka.commy_id, prokuror_id = troyka.prokuror_id)
    db.add(troykaModel)
    db.commit()
    return {"message": troyka}
@app.get("/troyka/{id}")
def getTroykaByID(id: int):
    troyka = db.get(TroykaModel, id)
    return {"RabOfGod": troyka}
@app.get("/troyka")
def getTroykas():
    troykas = db.query(TroykaModel).all()
    return {"RabOfGod[]": troykas}

@app.post("/sentence")
def addSentence(sentence: Sentence):
    sentenceModel = SentenceModel(troyka_id = sentence.troyka_id, description = sentence.description,
                               ifExecution = sentence.ifExecution)
    db.add(sentenceModel)
    db.commit()
    return {"message": sentence}
@app.get("/sentence/{id}")
def getSentenceByID(id: int):
    sentence = db.get(SentenceModel, id)
    return {"Sentence": sentence}
@app.get("/sentence")
def getSentences():
    sentences = db.query(SentenceModel).all()
    return {"Sentence[]": sentences}

@app.delete("/sentence/{id}")
def deleteSentenceByID(id: int):
    sentence = db.get(SentenceModel, id)
    db.delete(sentence)
    db.commit()
    return {"Sentence": sentence}

@app.get("/file", response_class = FileResponse)
def root_html():
    return "Files/Stalin.jpg"



