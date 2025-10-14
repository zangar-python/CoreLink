from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from domain.services.wiki_service.wiki_crud_service import WikiService
from domain.services.wiki_service.wiki_create_celery import start_celery_worker_CREATE_WIKI

from domain.services.wiki_service.wiki_change_celery import WikiChange_Controller

from infrastructure.db.connection_users_repo.req_to_change_crud import Req_To_Change_Repo
from api.serializers.wiki_serializer import Reques_to_change_serializer



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
    def get(self,request:Request,req_id:int):
        res = Req_To_Change_Repo(request.user).get_request(req_id)
        if not res:
            res = Req_To_Change_Repo(request.user).get_my_request(req_id)
            if not res:
                return Response({"err":"Вы не можете увидить этот запрос!!!"})
        return Response(Reques_to_change_serializer(res).data)
    def delete(self,request:Request,req_id:int):
        res = WikiChange_Controller(request.user).delete_request_change(req_id)
        return Response(res)
class get_all_my_req_changes(APIView):
    def get(self,request:Request):
        res = WikiChange_Controller(request.user).my_changes()
        return Response(Reques_to_change_serializer(res,many=True).data)
class get_all_req_changes(APIView):
    def get(self,request:Request):
        res = WikiChange_Controller(request.user).get_changes()
        return Response(Reques_to_change_serializer(res,many=True).data)
    def delete(self,request:Request):
        repo = Req_To_Change_Repo(request.user)
        repo.clear_all_requests()
        return Response({
            "Clered":True,
            "user_id":request.user.id
        })