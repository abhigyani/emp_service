from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from settings import get_settings
from database import engine
from models import Base

oauth2 = OAuth2PasswordBearer(tokenUrl="token")

settings = get_settings()
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/test")
async def test(token: Annotated[str, Depends(oauth2)]):
    return "test"


@app.get("/hello")
async def hello_world():
    return "Hello World!"
