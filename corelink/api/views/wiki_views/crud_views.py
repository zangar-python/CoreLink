from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from domain.services.wiki_service.wiki_crud_service import WikiService
from domain.services.wiki_service.wiki_create_celery import start_celery_worker_CREATE_WIKI

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
