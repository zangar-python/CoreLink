from django.contrib.auth.models import User
from infrastructure.tasks.req_to_change_async import set_request_to_change,delete_request_change,accept_request_to_change

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
    