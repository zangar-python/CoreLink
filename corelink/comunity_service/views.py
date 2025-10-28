from .services.main_service import ComunityService,MessageService,ComunityUserService


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from django.contrib.auth.models import User

class Comunity_main_views(APIView):
    def get(self,request:Request):
        return Response(ComunityService(request).get_comunitys())
    def post(self,request:Request):
        return Response(ComunityService(request).set_comunity())
class Comunity_detail_views(APIView):
    def get(self,request:Request,pk:int):
        res = ComunityService(request).get_comunity(pk)
        return Response(res)
    def delete(self,request:Request,pk:int):
        res = ComunityService(request).delete_comunity(pk)
        return Response(res)
    def patch(self,request:Request,pk:int):
        res = ComunityService(request).put_comunity(pk)
        return Response(res)

class User_comunity_views(APIView):
    def post(self,request:Request,pk:int):
        service = ComunityUserService(request.user)
        is_cor = service.set_repo(pk)
        if not is_cor:
            return Response(False)
        res = service.add_user()
        return Response(res)
    def delete(self,request:Request,pk:int):
        service = ComunityUserService(request.user)
        is_cor = service.set_repo(pk)
        if not is_cor:
            return Response(False)
        res = service.remove_user()
        return Response(res)

class Ban_user_views(APIView):
    def post(self,request:Request,pk:int,user_pk:int):
        service = ComunityUserService(request.user)
        is_cor = service.set_repo(pk)
        if not is_cor:
            return Response(False)
        res = service.ban_user(user_pk)
        return Response(res)
class Message_comunity_views(APIView):
    def post(self,request:Request,pk:int):
        service = MessageService(request)
        is_cor = service.set_repo(pk)
        if not is_cor:
            return Response(False)
        res = service.set_message()
        return Response(res)
    def get(self,request:Request,pk:int):
        service = MessageService(request)
        is_cor = service.set_repo(pk)
        if not is_cor:
            return Response(False)
        res = service.get_messages()
        return Response(res)
class Message_detail_views(APIView):
    def get(self,request:Request,pk:int,msg_pk:int):
        service = MessageService(request)
        is_cor = service.set_repo(pk)
        if not is_cor:
            return Response(False)
        res = service.put_message(msg_pk)
        return Response(res)
    def patch(self,request:Request,pk:int,msg_pk:int):
        service = MessageService(request)
        is_cor = service.set_repo(pk)
        if not is_cor:
            return Response(False)
        res = service.put_message(msg_pk)
        return Response(res)