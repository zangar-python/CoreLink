from django.urls import path
from .views import classic_analytics_views,users_likes_wiki_views,user_recom_likes_views,user_recomend_V2_ORM_views,user_recom_by_tag

analitic_urls = [
    path("",classic_analytics_views.as_view(),name="numpy base"),
    path("wiki_likes/",users_likes_wiki_views.as_view(),name="users-wikis-likes"),
    path("likes/<int:id>/",user_recom_likes_views.as_view(),name="user-recomends"),
    path("likes-v2/",user_recomend_V2_ORM_views.as_view(),name="ORM liked recom"),
    path("tags/",user_recom_by_tag.as_view(),name="recom by tag")
]