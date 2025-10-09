from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from domain.services.user_auth import UserAuth_Log
from domain.services.user_profile import User_Profile_Service
from rest_framework.permissions import AllowAny

class UserRegisterViews(APIView):
    permission_classes = [AllowAny]
    def post(self,request:Request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        
        if not username or not email or not password:
            return {"err":"Введите данные имя пользователья,емайл,пароль"}
        return Response(UserAuth_Log().user_register(username,password,email))
class UserLoginViews(APIView):
    permission_classes = [AllowAny]
    def post(self,request:Request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        return Response(UserAuth_Log().user_login(password,email=email,username=username))
class UserProfile(APIView):
    def get(self,request:Request):
        profile_service = User_Profile_Service()
        return Response(profile_service.set_user_data(request))