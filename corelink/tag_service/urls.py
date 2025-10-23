from rest_framework.urls import path
from .views import get_all_tags_views,tag_info_views

tag_service_urls = [
    path("",get_all_tags_views.as_view(),name="get_all_tags"),
    path("<int:pk>/",tag_info_views.as_view(),name="get_tag_info")
]
