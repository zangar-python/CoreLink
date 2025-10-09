from django.contrib.auth.models import User
from rest_framework.authentication import authenticate
from typing import Union

class UserRepository:
    def __init__(self):
        pass
    def create_user(self,username,password,email) -> User:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email    
        )
        return user
    
    def login(self,password:str,username:Union[str,None]=None,email:Union[str,None]=None) -> User:
        if username is not None:
            return authenticate(username=username,password=password)
        elif email is not None:
            return authenticate(email=email,password=password)
        else:
            return False
    def get_user(self,id:Union[str,None]=None,username:Union[str,None]=None,email:Union[str,None]=None):
        if id is not None:
            return User.objects.get(id=id)
        if username is not None:
            return User.objects.get(username=username)
        elif email is not None:
            return User.objects.get(email=email)
        return None
    def user_exists(self,id:Union[str,None]=None,username:Union[str,None]=None,email:Union[str,None]=None) -> bool:
        result = False
        if id is not None:
            if User.objects.filter(id=id).exists():
                result = True
        if username is not None:
            if User.objects.filter(username=username).exists():
                result = True
        if email is not None:
            if User.objects.filter(email=email).exists():
                result = True
        else:
            return False
        return result