from rest_framework.views import APIView
from rest_framework.response import Response
from domain.services.user_rating import celery_start

class get_user_list(APIView):
    def get(self,request):
        return Response(celery_start.get_data())