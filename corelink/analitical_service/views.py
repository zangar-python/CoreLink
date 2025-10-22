from rest_framework.views import APIView
from .service import classic_numpy
from .service.recom_system import Recom_Wiki
from rest_framework.response import Response

class classic_analytics_views(APIView):
    def post(self,request):
        arr = request.data.get("arr",[0,0])
        return Response(classic_numpy.numpy_classis_analitics(arr))

class users_likes_wiki_views(APIView):
    def get(self,request):
        res = classic_numpy.get_users()
        return Response(res)

class user_recom_likes_views(APIView):
    def get(self,request,id:int):
        return Response(classic_numpy.user_likes_recomends(id))
class user_recomend_V2_ORM_views(APIView):
    def get(self,request):
        return Response(Recom_Wiki(request.user).get_our_like())