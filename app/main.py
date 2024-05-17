'''
Main module
'''
from typing import Annotated
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from settings import get_settings
import models
from database import engine

oauth2 = OAuth2PasswordBearer(tokenUrl="token")

settings = get_settings()
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/test")
async def test(token: Annotated[str, Depends(oauth2)]):
    '''
    Method
    '''
    return "test"


@app.get("/hello")
async def hello_world():
    '''
    Method
    '''
    return "Hello World!"
