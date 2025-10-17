from rest_framework.views import APIView
from .service import classic_numpy
from rest_framework.response import Response

class classic_analytics_views(APIView):
    def post(seld,request):
        arr = request.data.get("arr",[0,0])
        return Response(classic_numpy.numpy_classis_analitics(arr))