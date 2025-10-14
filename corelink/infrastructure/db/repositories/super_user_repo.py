# from rest_framework.request import Request
from django.contrib.auth.models import User
from django.db.models.manager import BaseManager
from typing import Union

class SuperUserRepository:
    def __init__(self,user:User):
        self.user = user
        pass
    def user_is_superuser(self,user:Union[User,None]=None) -> bool:
        if user is not None:
            return user.is_superuser
        return self.user.is_superuser
    
    def get_users(self) -> BaseManager[User]:
        if not self.user.is_superuser:
            return None
        users = User.objects.all()
        return users
    def get_users_join_activity(self):
        if not self.user.is_superuser:
            return None
        users = User.objects.select_related("activity")
        return users
    def delete_user(self,user:User):
        if not self.user.is_superuser:
            return False
        user.delete()
        return True
    def set_admin(self,user:User):
        if self.user.is_superuser:
            user.is_superuser = True
            user.save
            return True
        return False
    def remove_admin(self,user:User):
        if self.user.is_superuser:
            user.is_superuser = False
            user.save()
            return True
        return False