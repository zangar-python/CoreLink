from ..entitys.User_Profile import UserProfile
from rest_framework.request import Request
from api.serializers.user_serializer import UserSerializer

class User_Profile_Service:
    def __init__(self):
        pass
    def set_user_data(self,request:Request):
        user_profile = UserProfile(user=request.user)
        user_profile.set_user(
            username=request.data.get("username"),
            password=request.data.get("password"),
            email=request.data.get("email")
        )
        return UserSerializer(user_profile.get_user()).data