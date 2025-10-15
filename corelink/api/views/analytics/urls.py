from .user_top_by_likes_views import get_user_list



from django.urls import path

analytic_urls = [
    path("by_like/",get_user_list.as_view(),name="get user top by likes")
]