from infrastructure.db.repositories.user_repository import UserRepository
from infrastructure.db.repositories.token_repository import TokenRepository
from api.serializers.user_serializer import UserSerializer


from typing import Union

class UserAuth_Log:
    def __init__(self):
        pass
    def RESULT(self,data,is_error:bool=False):
        return {
            "data":data,
            "is_error":is_error
        }
    
    def user_register(self,username,password,email):
        if not username or not password or not email:
            return self.RESULT(
                {"err":"Введите данные {username,password,email}"},True
            )
        user_repos = UserRepository()
        if user_repos.user_exists(username=username,email=email,id=None):
            return self.RESULT(
                {"err":"Пользователь с таким именем/емайлом уже существует"}
            )
        user = user_repos.create_user(username,password,email)
        
        token_repos = TokenRepository()
        token = token_repos.create_or_get_tokenkey(user)
        
        return self.RESULT({
            "user":UserSerializer(user).data,
            "token_key":token.key
        })
    def user_login(self,password:str,email:Union[str,None]=None,username:Union[str]=None):
        if not username and not email:
            return self.RESULT({
                "err":"Данные пусты username/email"
            },True)
        if not password:
            return self.RESULT(
                {'err':'password is null'},True
            )
        user_repos = UserRepository()
        user = user_repos.login(password=password,username=username,email=email)
        print(user)
        if not user:
            return self.RESULT(
                {'err':"пользователи с такими данными не существует"},True
            )
        token_repos = TokenRepository()
        token = token_repos.create_or_get_tokenkey(user)
        return self.RESULT({
            "user":UserSerializer(user).data,
            "token_key":token.key
        })
    def get_user_by(self,id:Union[int,None]=None,username:Union[str,None]=None,email:Union[str,None]=None):
        user_repos = UserRepository()
        user_exists = user_repos.user_exists(id=id,username=username,email=email)
        if not user_exists:
            return self.RESULT(
                {"err":"Пользователь не существует"},True
            )
        user = user_repos.get_user(id=id,username=username,email=email)
        return self.RESULT({"user":UserSerializer(user).data})
    