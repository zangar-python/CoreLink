from typing import Union
from django.contrib.auth.models import User

class UserProfile:
    def __init__(self,user:User):
        self.user = user
        pass
    def get_user(self):
        return self.user
    def set_user(self,username:Union[str,None]=None,password:Union[str,None]=None,email:Union[str,None]=None):
        if username:
            self.user.username = username
        if password:
            self.user.password = password
        if email:
            self.user.email = email
        self.user.save()
        return True