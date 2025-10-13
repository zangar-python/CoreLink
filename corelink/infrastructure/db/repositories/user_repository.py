from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from typing import Union
from .activity_repo import ActivityRepository

class UserRepository:
    def __init__(self):
        pass
    def create_user(self,username,password,email) -> User:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email    
        )
        ActivityRepository(user).set_activity()
        return user
    
    def login(self,password:str,username:Union[str,None]=None,email:Union[str,None]=None) -> User:
        if username:
            user = authenticate(username=username,password=password)
            if user:
                print(user)
                ActivityRepository(user).set_activity()
            return user
        elif email:
            user = authenticate(email=email,password=password)
            if user:
                print(user)
                ActivityRepository(user).set_activity()
            return user
        else:
            print("err")
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
        if id:
            if User.objects.filter(id=id).exists():
                result = True
        elif username:
            if User.objects.filter(username=username).exists():
                result = True
        elif email:
            if User.objects.filter(email=email).exists():
                result = True
        else:
            return False
        return result