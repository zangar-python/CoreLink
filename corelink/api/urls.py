from .views.user_views import UserLoginViews,UserRegisterViews,UserProfile,UserStoryViews
from .views.admin_views import Get_users_list,Delete_all_active,Delete_user,Top_wikis_set,Wiki_count_analys,User_total_likes_count_set
from .views.wiki_views.crud_views import Wiki_CRUD_Views,Wiki_Detail_CRUD_View,Wiki_set_delete_like
from .views.wiki_views.recomendations_views import Wiki_Top

from .views.wiki_views.req_to_change_views import Req_to_change_set_views,Accept_for_req_changes,get_all_my_req_changes,get_all_req_changes

from django.urls import path,include

req_change_urls = [
    path("<int:req_id>/",Accept_for_req_changes.as_view()),
    path("",get_all_req_changes.as_view()),
    path("my/",get_all_my_req_changes.as_view())
]

user_views_urls = [
    path("register/",UserRegisterViews.as_view(),name="user-register"),
    path("login/",UserLoginViews.as_view(),name="user-login"),
    path("",UserProfile.as_view(),name="User-profile"),
    path("story/",UserStoryViews.as_view(), name="story"),
]
admin_views_urls = [
    path("users/",Get_users_list.as_view(),name="users-list"),
    path("top/",Top_wikis_set.as_view(),name="set_top_wiki"),
    path("del-active/",Delete_all_active.as_view(),name="delete-activity-active"),
    path("del-user/<int:id>/",Delete_user.as_view(),name="delte-user"),
    path("wiki-count/",Wiki_count_analys.as_view(),name="Wiki analys users"),
    path("user-likes/",User_total_likes_count_set.as_view(),name="users total likes rating")
]
wiki_views_urls = [
    path("",Wiki_CRUD_Views.as_view(),name="POST GET Wiki"),
    path("<int:id>/",Wiki_Detail_CRUD_View.as_view(),name="GET PATCH DELETE"),
    path("<int:id>/like/",Wiki_set_delete_like.as_view(),name="set or delete like from wiki"),
    path("top/",Wiki_Top.as_view(),name="TOP WIKI FOR A DAY"),
    path("<int:wiki_id>/change/",Req_to_change_set_views.as_view(),name="test")
]

from .views.analytics.urls import analytic_urls


api_urls = [
    path("",include(user_views_urls)),
    path("admin/",include(admin_views_urls)),
    path("wiki/",include(wiki_views_urls)),
    path("change/",include(req_change_urls)),
    path("analytics/",include(analytic_urls))
]
