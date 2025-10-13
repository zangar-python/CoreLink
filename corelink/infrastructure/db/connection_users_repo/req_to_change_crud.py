from infrastructure.models import Request_To_Change_Wiki,Wiki
from typing import Union
from django.contrib.auth.models import User
from django.db.models.manager import BaseManager

class Req_To_Change_Repo:
    def __init__(self,user:User):
        self.user = user
        pass
    def set_request(self,wiki:Wiki,title:str,text:str):
        Request_To_Change_Wiki.objects.create(
            wiki=wiki,
            title=title,
            text=text,
            to_author=wiki.author,
            from_user=self.user   
        )
        return
    
    # GET REQUESTS LIST
    def get_requests_list(self,wiki:Union[Wiki,None]) -> BaseManager[Request_To_Change_Wiki]:
        if wiki:
            requests = self.user.requests_to_change.filter(wiki=wiki).order_by("-created_at")
        else:
            requests = self.user.requests_to_change.all().order_by("-created_at")
        return requests
    
    def get_my_requests_list(self,wiki:Union[Wiki,None]) -> BaseManager[Request_To_Change_Wiki]:
        if wiki:
            my_requests = self.user.my_requests_to_change.filter(wiki=wiki).order_by("-created_at")
        else:
            my_requests = self.user.my_requests_to_change.all().order_by("-created_at")
        return my_requests
    
    
    # EXIST REQUESTS?
    def request_exists(self,id):
        if self.user.requests_to_change.filter(id=id).exists():
            return True
        return False
    def my_request_exists(self,id):
        if self.user.my_requests_to_change.filter(id=id).exists():
            return True
        return False
    
    #REQUEST MANIPULATIONS
    def delete_my_request(self,id):
        if not self.my_request_exists(id):
            return False
        self.user.my_requests_to_change.get(id=id).delete()
        return True
    def get_my_request(self,id) -> Union[Request_To_Change_Wiki,None]:
        if not self.my_request_exists(id):
            return 
        return self.user.my_requests_to_change.get(id=id)
    def get_request(self,id) -> Union[Request_To_Change_Wiki,None]:
        if not self.request_exists(id):
            return
        return self.user.requests_to_change(id)
    
    #   CLEAR ALL MESSAGES
    def clear_all_messages(self):
        self.user.requests_to_change.all().delete()
        return
    def clear_all_my_messages(self):
        self.user.my_requests_to_change.all().delete()
        return
        