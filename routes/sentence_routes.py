from fastapi import APIRouter
from models.Sentence import Sentence
from DataBase.DBDeclaration import SentenceModel
from DataBase.DBget import db


router = APIRouter()


@router.post("/sentence")
def addSentence(sentence: Sentence):
    sentenceModel = SentenceModel(troyka_id = sentence.troyka_id, description = sentence.description,
                               ifExecution = sentence.ifExecution)
    db.add(sentenceModel)
    db.commit()
    return {"message": sentence}


@router.get("/sentence/{id}")
def getSentenceByID(id: int):
    sentence = db.get(SentenceModel, id)
    return {"Sentence": sentence}


@router.get("/sentence")
def getSentences():
    sentences = db.query(SentenceModel).all()
    return {"Sentence[]": sentences}


@router.delete("/sentence/{id}")
def deleteSentenceByID(id: int):
    sentence = db.get(SentenceModel, id)
    db.delete(sentence)
    db.commit()
    return {"Sentence": sentence}