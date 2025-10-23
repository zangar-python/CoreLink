from ..models import Tag,Wiki
from django.shortcuts import get_object_or_404
from infrastructure.db.wiki_repositories.crud import WikiRepository
from django.db.models.manager import BaseManager

from typing import Union

class Tag_Wiki_Repo:
    def __init__(self):
        pass
    def set_or_get_tag(self,name:str):
        tag,_ = Tag.objects.get_or_create(name=name)
        return tag
    def set_tag_with_wiki(self,name:str,wiki:Wiki):
        tag = self.set_or_get_tag(name=name)
        if tag.wikis.filter(pk=wiki.pk).exists():
            return 
        print(wiki)
        tag.wikis.add(wiki)
        tag.save()
        print(tag.wikis.values("id"))
        return True
    def delete_wiki_from_tag(self,id_tag,wiki:Wiki):
        tag = get_object_or_404(Tag,pk=id_tag)
        if not tag.wikis.filter(pk=wiki.pk).exists():
            return False
        tag.wikis.remove(wiki)
        return True
    def get_tag(self,pk:Union[int,None]=None,name:Union[str,None]=None):
        if pk:
            if Tag.objects.filter(pk=pk).prefetch_related("wikis").exists():
                return Tag.objects.get(pk=pk)
        if name:
            if Tag.objects.filter(name=name).prefetch_related("wikis").exists():
                return Tag.objects.get(name=name)
        return None
    def add_tags(self,wiki:Wiki,tags_name:list[str]):
        if not tags_name:
            return False
        for name in tags_name:
            self.set_tag_with_wiki(name,wiki)
        return wiki.pk
    def delete_tag(self,pk:Union[int,None]=None,name:Union[str,None]=None):
        tag = self.get_tag(pk,name)
        if not tag:
            return False
        tag.delete()
        return True
    def get_tag_info(self,tag:Tag):
        tag_info = {
            "pk":tag.pk,
            "name":tag.name,
            "wikis":tag.wikis.values("id","title","created_at","author")
        }
        # for wiki in tag.wikis.all():
            # if wiki:
            #     wiki_info = wiki.values("id","name","created_at","author")
            #     tag_info["wikis"].append(wiki_info)
            # else:
            #     tag_info["wikis"].append(None)
        return tag_info
    def get_wiki_tags(self,wiki:Wiki) -> BaseManager[Tag]:
        return wiki.tags.all()
    def get_tags_wikis(self,tag:Tag) -> BaseManager[Wiki]:
        return tag.wikis.all()
    def get_tags(self) -> BaseManager[Tag]:
        return Tag.objects.all()
    