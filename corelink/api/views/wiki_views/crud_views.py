from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from domain.services.wiki_service.wiki_crud_service import WikiService
from domain.services.wiki_service.wiki_create_celery import start_celery_worker_CREATE_WIKI

from domain.services.wiki_service.wiki_change_celery import WikiChange_Controller

from infrastructure.db.connection_users_repo.req_to_change_crud import Req_To_Change_Repo
from api.serializers.wiki_serializer import Reques_to_change_serializer

class Wiki_CRUD_Views(APIView):
    def post(self,request:Request):
        title = request.data.get("title")
        text = request.data.get("text")
        
        if not text or not title:
            return Response("Пополните поля {text,title}",status=401) 
        return Response(start_celery_worker_CREATE_WIKI(request.user,title,text))
    def get(self,request:Request):
        res = WikiService(request.user).get_all_wiki()
        return Response(res)
class Wiki_Detail_CRUD_View(APIView):
    def get(self,request:Request,id:int):
        res = WikiService(request.user).get_wiki(id=id)
        return Response(res)
    def patch(self,request:Request,id:int):
        title = request.data.get("title")
        text = request.data.get("text")
        
        if not title and not text:
            return Response("У вас поля пустые!")
        res = WikiService(request.user).update_wiki(id=id,title=title,text=text)
        return Response(res)
    def delete(self,request:Request,id:int):
        res = WikiService(request.user).delete_wiki(id=id)
        return Response(res)

class Req_to_change_set_views(APIView):
    def post(self,request:Request,wiki_id):
        
        title = request.data.get("title")
        text = request.data.get("text")
        res = WikiChange_Controller(request.user).set_change(wiki_id,title,text)
        return Response(res)
class Accept_for_req_changes(APIView):
    def post(self,request:Request,req_id:int):
        res = WikiChange_Controller(request.user).accept_request_change(req_id)
        return Response(res)
class get_all_req_changes(APIView):
    def get(self,request:Request):
        res = Req_To_Change_Repo(request.user).get_requests_list()
        return Response(Reques_to_change_serializer(res,many=True).data)

