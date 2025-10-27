from .repository import Message_Repository,ComunityRepository,Comunity_base_Repository
from .repository import Message,Comunity
from infrastructure.db.repositories.user_repository import UserRepository
from infrastructure.db.repositories.activity_repo import ActivityRepository

from api.serializers.comunity_serializers import MessageSerializer,ComunitySerializer


from rest_framework.request import Request

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
        if len(name) > 200:
            return False
        res = self.base_repo.create_comunity(name,description)
        if not res:
            return False
        ActivityRepository(self.request.user).update(10)
        return ComunitySerializer(res).data
    
    def get_comunity(self,pk):
        res = self.base_repo.get_comunity(pk)
        if not res:
            return False
        return ComunitySerializer(res).data
    
    def delete_comunity(self,pk):
        return self.base_repo.delete_comunity(pk)
    
    def put_comunity(self,pk):
        comunity = self.base_repo.get_comunity(pk)
        if not comunity:
            return False
        repo = ComunityRepository(self.request.user,comunity)
        
        name = self.request.data.get("name")
        if name:
            if len(name) > 200:
                return False
        description = self.request.data.get("description")
        res = repo.put_comunity(name,description)
        if not res:
            return False
        ActivityRepository(self.request.user).update(5)
        return ComunitySerializer(res).data

class ComunityUserService:
    def __init__(self,user):
        self.user = user
        self.base_repo = Comunity_base_Repository(user)
        self.comunity_repo = None
        pass
    def set_repo(self,pk):
        comunity = self.base_repo.get_comunity(pk)
        if not comunity:
            return False
        self.comunity_repo = ComunityRepository(self.user,comunity)
        return True
    
    def add_user(self):
        res = self.comunity_repo.add_user()
        if not res:
            return False
        ActivityRepository(self.user).update(5)
        return ComunitySerializer(res).data
    
    def remove_user(self):
        return ComunitySerializer(self.comunity_repo.remove_user()).data
    
    def ban_user(self,pk):
        user = UserRepository().get_user(id=pk)
        if not user:
            return False
        res = self.comunity_repo.ban_user(user)
        return res

class MessageService:
    def __init__(self,request):
        self.request = request
        self.base_repo = Comunity_base_Repository(request.user)
        self.msg_repo = None
        pass
    def set_repo(self,pk):
        comunity = self.base_repo.get_comunity(pk)
        if not comunity:
            return False
        self.msg_repo = Message_Repository(self.request.user,comunity)
        return True
    
    def set_message(self):
        text = self.request.data.get("text")
        if not text:
            return False
        res = self.msg_repo.add_message(text)
        if not res:
            return False
        ActivityRepository(self.request.user).update(1)
        return MessageSerializer(res).data
    
    def get_messages(self):
        return MessageSerializer(self.msg_repo.get_messages(),many=True).data
    
    def put_message(self,pk_message,text):
        message = self.msg_repo.get_message(pk_message)
        if not message:
            return False
        text = self.request.data.get("text")
        if not text:
            return False
        res = self.msg_repo.put_message(message,text)
        if not res:
            return res
        ActivityRepository(self.request.user).update(1)
        return MessageSerializer(res).data
    def get_message(self,pk):
        res = self.msg_repo.get_message(pk)
        if not res:
            return False
        return MessageSerializer(res).data
        