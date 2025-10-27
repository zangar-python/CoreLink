from ..models import Comunity,Message,User
from django.db.models.manager import BaseManager
from typing import Union

class Comunity_base_Repository:
    def __init__(self,user:User):
        self.user = user
        pass
    def comunity_with_name_exists(self,name):
        return Comunity.objects.filter(name=name).exists()
    
    def create_comunity(self,name,description):
        is_exists = self.comunity_with_name_exists(name)
        if is_exists:
            return False
        comunity = Comunity.objects.create(
            name=name,
            description=description,
            admin=self.user
        )
        return comunity
    def delete_comunity(self,pk):
        is_exists = Comunity.objects.filter(pk=pk).exists()
        if not is_exists:
            return False
        comunity = Comunity.objects.get(pk=pk)
        if comunity.admin != self.user:
            return False
        comunity.delete()
        return True
    def get_comunity(self,pk):
        if not Comunity.objects.filter(pk=pk):
            return False
        return Comunity.objects.get(pk=pk)

class ComunityRepository(Comunity_base_Repository):
    def __init__(self,user:User,comunity:Comunity):
        super().__init__(user)
        self.comunity = comunity
        self.is_admin = comunity.admin == user
        pass
    def add_user(self):
        if self.is_admin:
            return False
        self.comunity.users.add(self.user)
        return self.comunity
    def remove_user(self):
        self.comunity.users.delete(self.user)
        return self.comunity
    def ban_user(self,user_to_ban:User):
        if not self.is_admin:
            return False
        self.comunity.users.remove(user_to_ban)
        return True
    def put_comunity(self,name:Union[str,None]=None,description:Union[str,None]=None):
        if not self.is_admin:
            return False
        if name:
            self.comunity.name = name
        if description:
            self.comunity.description = description
        self.comunity.save()
        return self.comunity

class Message_Repository(ComunityRepository):
    def __init__(self,user:User,comunity:Comunity):
        super().__init__(user,comunity)
        pass
    def is_user(self):
        if not self.is_admin:
            return self.comunity.users.filter(pk=self.user.pk).exists()
        return True
    def add_message(self,text):
        if not self.is_user():
            return False
        message = Message.objects.create(
            text = text,
            comunity = self.comunity,
            from_user = self.user
        )
        return message
    def get_messages(self) -> BaseManager[Message]:
        return self.comunity.messages.all().order_by("-created_at")
    def get_message(self,pk) -> Message:
        if not self.comunity.messages.filter(pk=pk).exists():
            return False
        return self.comunity.messages.get(pk=pk)
    def delete_message(self,message:Message):
        if not self.is_admin:
            if not message.from_user != self.user:
                return False
        message.delete()
        return True
    def put_message(self,message:Message,text:str):
        if not message.from_user == self.user:
            return False
        message.text = text
        message.save()
        return message