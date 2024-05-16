'''
User Model Class
'''
from typing import Union
from pydantic import BaseModel


class User(BaseModel):
    '''
    User Model class
    '''
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disable: Union[bool, None] = None
