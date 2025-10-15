from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from domain.services.wiki_service.wiki_crud_service import WikiService

class Wiki_Top(APIView):
    def get(self,request:Request):
        res = WikiService(request.user).top_wiki_get()
        return Response(res)