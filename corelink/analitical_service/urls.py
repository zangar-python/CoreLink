from django.urls import path
from .views import classic_analytics_views

analitic_urls = [
    path("",classic_analytics_views.as_view(),name="numpy base")
]