from .repository import Message_Repository,ComunityRepository,Comunity_base_Repository
from .repository import Message,Comunity

from api.serializers.comunity_serializers import MessageSerializer,ComunitySerializer

from rest_framework.request import Request
from typing import Union

class ComunityService:
    def __init__(self,request:Request):
        self.request = request
        self.base_repo = Comunity_base_Repository(request.user)
        pass
    
    def set_comunity(self):
        name = self.request.data.get("name")
        description = self.request.data.get("description","")
        if not name:
            return False
        res = self.base_repo.create_comunity(name,description)
        if not res:
            return False
        return ComunitySerializer(res).data
    
    def get_comunity(self,pk):
        res = self.base_repo.get_comunity(pk)
        if not res:
            return False
        return ComunitySerializer(res).data
    
        
        