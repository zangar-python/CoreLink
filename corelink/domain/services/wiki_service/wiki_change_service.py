from typing import Union
from infrastructure.db.repositories.user_repository import UserRepository,User
from infrastructure.db.connection_users_repo.req_to_change_crud import Req_To_Change_Repo
from infrastructure.db.wiki_repositories.crud import WikiRepository
from infrastructure.db.repositories.activity_repo import ActivityRepository

class RequestToChangeWiki:
    def __init__(self,user_id):
        self.user_repo = UserRepository()
        self.user_id = user_id
        self.user = None
        self.req_repo = None
        self.wiki_repo = None
        print("Обьект создан")
        pass
    def set_user(self):
        # if not User.objects.filter(id=self.user_id).exists():
        if not UserRepository().user_exists(self.user_id):
            return False
        self.user =  self.user_repo.get_user(id=self.user_id)
        print("User is get")
        return True
    def set__repo(self):
        
        self.req_repo = Req_To_Change_Repo(self.user)
        self.wiki_repo = WikiRepository(self.user)
        print("Repo settings")
    def set_wiki_request(self,wiki_id,title:Union[str,None],text:Union[str,None]):
        wiki = self.wiki_repo.get_wiki(id=wiki_id)
        print(wiki.id,"wiki ID")
        if not wiki:
            print("wiki is not founded")
            return "Wiki not founded"
        if len(title) > 200:
            print("len title > 200")
            return f"Title > 200 {len(title)}"
        if self.user.id == wiki.author.id:
            print("автор")
            # ИЗМЕНЕНИЕ ДАННЫХ СРАЗУ БЕЗ ЗАПРОСА
            self.wiki_repo.update_wiki(wiki_id,title=title,text=text)
            return "Данные сменились без запроса"
        print("Add")
        change = self.req_repo.set_request(
            wiki=wiki,
            title=title,
            text=text,
        )
        print("ADDED")
        return {
            "req_change":{
                "wiki_id":change.wiki.id,
                "title":change.title,
                "text":change.text,
                "from_user":change.from_user.id,
                "to_author":change.to_author.id,
                "id":change.id
            }
        }
    
    def add_activity(self,user:User,ball:Union[int,None]=None):
        return ActivityRepository(user).update(ball)
    
    def ACCEPT_REQUEST_CHANGE(self,request_id):
        if not self.set_user():
            return False
        self.set__repo()
        request_change = self.req_repo.get_request(request_id)
        if not request_change:
            return False
        wiki = request_change.wiki
        if self.user.id is not wiki.author.id:
            return False
        wiki.title = request_change.title
        wiki.text = request_change.text
        wiki.save()
        request_change.delete()
        self.add_activity(request_change.from_user,40)
        self.add_activity(wiki.author,20)
        return True
    
    def DELETE_REQUEST_CHANGE(self,req_id):
        if not self.set_user():
            return False
        self.set__repo()
        request_change = self.req_repo.get_request(req_id)
        if not request_change:
            return False
        if request_change.to_author.id is not self.user.id:
            return False
        request_change.delete()
        return True
    
    def SET_REQUEST_TO_CHANGE(self,wiki_id,title:Union[str,None]=None,text:Union[str,None]=None):
        if not self.set_user():
            print("False user set")
            return "Пользователь не найден"
        self.set__repo()
        self.add_activity(self.user,20)
        return self.set_wiki_request(wiki_id=wiki_id,title=title,text=text)