from django.contrib.auth.models import User
from infrastructure.tasks.req_to_change_async import set_request_to_change,delete_request_change,accept_request_to_change
from infrastructure.db.connection_users_repo.req_to_change_crud import Req_To_Change_Repo
from typing import Union
from infrastructure.db.wiki_repositories.crud import WikiRepository


class WikiChange_Controller:
    def __init__(self,user:User):
        self.user = user
        pass
    def set_change(self,wiki_id,title,text):
        print("Таск щас вызвется")
        set_request_to_change.delay(self.user.id,wiki_id=wiki_id,title=title,text=text)
        print("Task is downed")
        return "Ваш запрос на обработке подождите пожалуйста"
    def delete_request_change(self,req_id):
        delete_request_change.delay(self.user.id,req_id)
        return "Ваш запрос на обработке"
    def accept_request_change(self,req_id):
        accept_request_to_change.delay(self.user.id,request_id=req_id)
        return "Ваш запрос на бработке"
    def my_changes(self,wiki_id:Union[int,None]=None):
        req_repo = Req_To_Change_Repo(self.user)
        if wiki_id:
            wiki = WikiRepository(self.user).get_wiki(wiki_id)
            return req_repo.get_my_requests_list(wiki)
        return req_repo.get_my_requests_list()
    def get_changes(self,wiki_id:Union[int,None]=None):
        req_repo = Req_To_Change_Repo(self.user)
        if wiki_id:
            wiki = WikiRepository(self.user).get_wiki(wiki_id)
            return req_repo.get_requests_list(wiki)
        return req_repo.get_requests_list()