from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from domain.services.admin_func import Admin_class_func
from rest_framework.permissions import IsAdminUser

class Get_users_list(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request:Request):
        return Response(Admin_class_func().get_users(request.user))
class Delete_user(APIView):
    permission_classes = [IsAdminUser]
    def delete(self,request:Request,id:int):
        return Response(Admin_class_func().delete_user(request.user,id=id))
class Top_wikis_set(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request:Request):
        return Response(Admin_class_func().set_top_wikis(request.user))
class Delete_all_active(APIView):
    permission_classes = [IsAdminUser]
    def delete(self,request:Request):
        return Response(Admin_class_func().delete_all_active(request.user))