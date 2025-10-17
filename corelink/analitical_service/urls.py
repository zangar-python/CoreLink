from django.urls import path
from .views import classic_analytics_views,users_likes_wiki_views

analitic_urls = [
    path("",classic_analytics_views.as_view(),name="numpy base"),
    path("wiki_likes/",users_likes_wiki_views.as_view(),name="users-wikis-likes")
]