from rest_framework.views import APIView
from .service import classic_numpy
from rest_framework.response import Response

class classic_analytics_views(APIView):
    def post(self,request):
        arr = request.data.get("arr",[0,0])
        return Response(classic_numpy.numpy_classis_analitics(arr))

class users_likes_wiki_views(APIView):
    def get(self,request):
        res = classic_numpy.get_users_wiki_likes()
        return Response(res)