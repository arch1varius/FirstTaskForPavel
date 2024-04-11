from fastapi import APIRouter
from fastapi import Depends
from models.GodSlave import RabOfGod
from DataBase.DBDeclaration import PolitburoModel
from DataBase.DBget import db
from deps import get_current_user


router = APIRouter()


@router.post('/politburo')
def politburo(text: str, user: RabOfGod = Depends(get_current_user)):

    if not user.ifTrockist:
        politburoModel = PolitburoModel(description=text)
        db.add(politburoModel)
        db.commit()
        return {"message": "sucessful done smth with politburo"}
    else:
        return {"message": "ААААААА ТРОЦКИСТЫЫЫЫ!!!!!"}


@router.get('/politburo')
def politburo(user: RabOfGod = Depends(get_current_user)):
    if not user.ifTrockist:
        politburo_data = db.query(PolitburoModel).all()
        return politburo_data
    else:
        return {"message": "ААААААА ТРОЦКИСТЫЫЫЫ!!!!!"}
