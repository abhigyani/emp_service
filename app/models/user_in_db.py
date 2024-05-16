'''
User in DB
'''
from models.users import User


class UserInDB(User):
    '''
    User in DB class.
    '''
    hashed_password: str
