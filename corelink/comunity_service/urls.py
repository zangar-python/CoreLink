from django.urls import path
from .views import Comunity_main_views,Comunity_detail_views,User_comunity_views,Ban_user_views,Message_comunity_views,Message_detail_views

community_urls = [
    path("",Comunity_main_views.as_view(),name="post get"),
    path("<int:pk>/",Comunity_detail_views.as_view(),name="det delete patch"),
    path("<int:pk>/user/",User_comunity_views.as_view(),name="post delete"),
    path("<int:pk>/ban/<int:user_pk>/",Ban_user_views.as_view(),name="post"),
    path("<int:pk>/message/",Message_comunity_views.as_view(),name="post get"),
    path("<int:pk>/message/<int:msg_pk>/",Message_detail_views.as_view(),name="put get")
]