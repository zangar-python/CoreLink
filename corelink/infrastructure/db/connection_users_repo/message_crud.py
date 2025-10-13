from infrastructure.models import Message
from typing import Union
from django.contrib.auth.models import User
from django.db.models.manager import BaseManager

class MessageRepo:
    def __init__(self,user:User):
        self.user = user
        pass
    def set_message(self,title:str,to_user:User,text:Union[str,None]) -> None:
        Message.objects.create(
            title=title,
            to_user=to_user,
            from_user=self.user,
            text=text
        )
        return 
    def get_my_messages(self) -> BaseManager[Message]:
        messages = self.user.my_messages.all().order_by("-created-at")
        return messages
    def clear_all_messages(self) -> None:
        self.user.messages.all().delete()
        return 
    def get_messages(self) -> BaseManager[Message]:
        messages = self.user.messages.all().order_by('-created_at')
        return messages
    def get_message(self,id) -> Union[Message,None]:
        message_exists = self.user.messages.filter(id=id).exists()
        if not message_exists:
            return 
        return self.user.messages.get(id=id)
    def get_my_message(self,id) -> Union[Message,None]:
        if not self.user.my_messages.filter(id=id).exists():
            return
        return self.user.my_messages.get(id=id)
    def get_messages_from_user(self,user:User) -> BaseManager[Message]:
        return self.user.messages.filter(from_user=user).order_by("-created_at")
    def get_my_messages_to_user(self,user:User) -> BaseManager[Message]:
        return self.user.my_messages.filter(to_user=user).order_by("-created_at")