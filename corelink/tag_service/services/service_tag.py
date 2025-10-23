from .repo_tag import Tag_Wiki_Repo
# from rest_framework.request import Request
from infrastructure.models import Wiki

from api.serializers.tag_serializers import TagSerializer

class Tag_Service:
    def __init__(self):
        self.repo = Tag_Wiki_Repo()
        pass
    def set_tags_list(self,wiki:Wiki,tags:list[str]):
        try:
            return self.repo.add_tags(wiki,tags)
        except Exception as e:
            print(e)
            return e
    
    def get_tags(self):
        tags = self.repo.get_tags()
        return TagSerializer(tags,many=True).data
    def get_tag_info(self,pk):
        tag = self.repo.get_tag(pk)
        tag_info = self.repo.get_tag_info(tag)
        return tag_info
    def delete_tag(self,pk):
        return {"data":f"Успешно удалено pk:{pk}"} if self.repo.delete_tag(pk) else {"err":f"Тег с pk:{pk} не найдено"}