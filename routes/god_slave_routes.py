from fastapi import APIRouter
from models.GodSlave import RabOfGod
from DataBase.DBDeclaration import GodSlaveModel
from DataBase.DBget import db


router = APIRouter()

@router.get("/slave")
def getSlaves():
    slaves = db.query(GodSlaveModel).all()
    return {"RabOfGod[]": slaves}

@router.patch("/slave/{id}")
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