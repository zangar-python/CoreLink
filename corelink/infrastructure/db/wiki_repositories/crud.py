from infrastructure.models import Wiki
from django.contrib.auth.models import User
from ..repositories.activity_repo import ActivityRepository
from typing import Union

class WikiRepository:
    def __init__(self,user:User):
        self.user = user
    def create_wiki(self,title,text):
        wiki = Wiki.objects.create(
            title=title,
            text=text,
            author=self.user
        )
        ActivityRepository(self.user).update(15)
        return wiki
    def get_wiki_with_author(self,id):
        if not Wiki.objects.filter(id=id).exists():
            return
        wiki = Wiki.objects.select_related("author").get(id=id)
        return wiki
    def get_wiki(self,id):
        if not Wiki.objects.filter(id=id).exists():
            return
        wiki = Wiki.objects.get(id=id)
        return wiki
    def update_wiki(self,id:int,title:Union[str,None]=None,text:Union[str,None]=None):
        if not self.user.my_wiki.filter(id=id).exists():
            return
        wiki = Wiki.objects.get(id=id)
        if title:
            if len(title) > 200:
                return
            wiki.title = title
        if text:
            wiki.text = text
        wiki.save()
        ActivityRepository(self.user).update(10)
        return wiki
    def get_all_wikis_with_author(self):
        wikis_with_author = Wiki.objects.select_related("author")
        return wikis_with_author
    def get_all_wikis(self):
        wikis = Wiki.objects.all()
        return wikis
    def delete_wiki(self,wiki:Wiki):
        wiki.delete()
        return