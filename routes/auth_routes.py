from fastapi import APIRouter
from fastapi import FastAPI, status, HTTPException, Depends
from models.GodSlave import RabOfGod
from models.Login_Data import Login_Data
from DataBase.DBDeclaration import GodSlaveModel
from DataBase.DBget import db
from auth.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)
from deps import get_current_user


router = APIRouter()


@router.post("/signup")
def signup_user(user: RabOfGod):
    user_in_db = db.query(GodSlaveModel).filter(GodSlaveModel.login == user.login).first()
    if user_in_db is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this login already exist"
        )
    user.password = get_hashed_password(user.password)
    user.login = user.login.lower()
    slaveModel = GodSlaveModel(login=user.login, password=user.password,
                               position = user.position, fullname = user.fullname,
                               photo_URL = user.photo_URL, ifTrockist = user.ifTrockist)

    db.add(slaveModel)
    db.commit()
    return {"message": user}


@router.post("/login")
async def login_user(form_data: Login_Data):
    form_data.login = form_data.login.lower()
    user = db.query(GodSlaveModel).filter(GodSlaveModel.login == form_data.login).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    hashed_passwd = user.password
    if not verify_password(form_data.password, hashed_passwd):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    return {
        "access_token": create_access_token(user.login),
        "refresh_token": create_refresh_token(user.login),
    }


@router.get('/me')
def get_me(user: RabOfGod = Depends(get_current_user)):
    return user