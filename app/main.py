'''
Main module
'''
from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2 = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


@app.get("/test")
async def test(token: Annotated[str, Depends(oauth2)]):
    return "test"


@app.get("/hello")
async def hello_world():
    return ("Hello World!")
