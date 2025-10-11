from infrastructure.db.wiki_repositories.crud import WikiRepository
from ..user_auth import UserAuth_Log
from api.serializers.wiki_serializer import WikiSerializer
from infrastructure.db.repositories.super_user_repo import SuperUserRepository

from typing import Union

class WikiService(UserAuth_Log):
    def __init__(self,user):
        self.user = user
        self.wiki_repo = WikiRepository(user)
        self.serializer = WikiSerializer
        self.super_user_repo = SuperUserRepository(self.user)
        pass
    
    def set_wiki(self,title:str,text:str):
        if len(title) > 200:
            return self.RESULT("title's length > 200",True)
        
        wiki = self.wiki_repo.create_wiki(title=title,text=text)
        return self.RESULT({
            "wiki":self.serializer(wiki).data,
            "created":True
        })
    def get_wiki(self,id):
        wiki_author = self.wiki_repo.get_wiki_with_author(id=id)
        if not wiki_author:
            return self.RESULT(f"wiki with id:{id} is not exists",True)
        wiki_serialized = self.serializer(wiki_author).data
        wiki_serialized["author_info"] = {
            "username":wiki_author.author.username,
            "id":wiki_author.author.id,
            "email":wiki_author.author.email,
        }
        return wiki_serialized
    def get_all_wiki(self):
        wikis_with_author = self.wiki_repo.get_all_wikis_with_author()
        result_wiki = []
        
        for wiki in wikis_with_author:
            wiki_data = {
                "wiki":{
                    "title":wiki.title,
                    "text":wiki.text,
                    "created_at":wiki.created_at.date(),
                    "updated_at":wiki.updated_at.date(),
                    "likes_count":wiki.likes.count(),
                    "id":wiki.id,
                    "author":{
                        "username":wiki.author.username,
                        "email":wiki.author.email,
                        "id":wiki.author.id,
                        "password":wiki.author.password,
                    }
                }
                
            }
            result_wiki.append(wiki_data)
        return result_wiki
        
    def update_wiki(self,id,title:Union[str,None]=None,text:Union[str,None]=None):
        if title and len(title) > 200:
            return self.RESULT("title length > 200!",True)
        wiki = self.wiki_repo.update_wiki(id=id,title=title,text=text)
        if not wiki:
            return self.RESULT(f"wiki with id:{id} is not exists",True)
        return self.get_wiki(wiki.id)
    
    def delete_wiki(self,id):
        wiki = self.wiki_repo.get_wiki(id)
        if not wiki:
            return self.RESULT(f"Wiki with id:{id} is not exists",True)
        if not wiki.author == self.user and not self.super_user_repo.user_is_superuser():
            return self.RESULT(f"У вас нету доступа чтобы удалить",True)
        self.wiki_repo.delete_wiki(wiki=wiki)
        return self.RESULT({
            "wiki":self.serializer(wiki).data,
            "deleted":True
        })