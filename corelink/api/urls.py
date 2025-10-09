from .views.user_views import UserLoginViews,UserRegisterViews,UserProfile
from django.urls import path,include

user_views_urls = [
    path("register/",UserRegisterViews.as_view(),name="user-register"),
    path("login/",UserLoginViews.as_view(),name="user-login"),
    path("",UserProfile.as_view(),name="User-profile")
]

api_urls = [
    path("",include(user_views_urls))
]
