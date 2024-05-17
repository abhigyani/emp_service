from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from db.session import engine, Base
from core.config import get_settings

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
