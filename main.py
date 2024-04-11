from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.file_routes import router as file_router
from routes.god_slave_routes import router as god_slave_router
from routes.politburo_routes import router as politburo_router
from routes.sentence_routes import router as sentence_router
from routes.troyka_routes import router as troyka_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(file_router)
app.include_router(god_slave_router)
app.include_router(politburo_router)
app.include_router(sentence_router)
app.include_router(troyka_router)