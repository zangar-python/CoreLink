# from ..entitys.User_Profile import UserProfile
from ..entitys.Activity_User import ActivityEntity
from rest_framework.request import Request
from api.serializers.user_serializer import UserSerializer
from api.serializers.activity_serializers import Activity
from django.contrib.auth.models import User
from infrastructure.cache.user_story import UserStory
from django.utils import timezone

class User_Profile_Service:
    def __init__(self):
        pass
    def set_user_data(self,request:Request):
        user_profile = ActivityEntity(user=request.user)
        user_profile.set_user(
            username=request.data.get("username"),
            password=request.data.get("password"),
            email=request.data.get("email")
        )
        # user_profile.set_active(5)
        # active = user_profile.get_active()
        return {
            "user":UserSerializer(user_profile.get_user()).data,
            # "active":ActivitySerializer(active).data
        }
    def get_user_profile(self,user:User):
        activity:Activity = user.activity
        if activity.active < 30:
            level = "low"
        elif 30<= activity.active < 70:
            level = "medium"
        else:
            level = "high"
        
        wiki_count = user.my_wiki.count()
        return {
            "username":user.username,
            "email":user.email,
            "id":user.id,
            "level_active":level,
            "activity":activity.active,
            "last_active":activity.last_active.date(),
            "wiki_count":wiki_count
        }
    def set_story(self,user_id,wiki_id):
        story = UserStory(user_id)
        story.SET_DATA(wiki_id)
        return 
    def get_story(self,user_id):
        story = UserStory(user_id)
        datas = story.GET_DATA()
        return datas
        