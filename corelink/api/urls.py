from .views.user_views import UserLoginViews,UserRegisterViews,UserProfile
from .views.admin_views import Get_users_list
from .views.wiki_views.crud_views import Wiki_CRUD_Views,Wiki_Detail_CRUD_View

from django.urls import path,include

user_views_urls = [
    path("register/",UserRegisterViews.as_view(),name="user-register"),
    path("login/",UserLoginViews.as_view(),name="user-login"),
    path("",UserProfile.as_view(),name="User-profile")
]
admin_views_urls = [
    path("users/",Get_users_list.as_view(),name="users-list")
]
wiki_views_urls = [
    path("",Wiki_CRUD_Views.as_view(),name="POST GET Wiki"),
    path("<int:id>/",Wiki_Detail_CRUD_View.as_view(),name="GET PATCH DELETE")
]

api_urls = [
    path("",include(user_views_urls)),
    path("admin/",include(admin_views_urls)),
    path("wiki/",include(wiki_views_urls))
]
