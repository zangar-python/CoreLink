from infrastructure.db.repositories.user_repository import UserRepository,User
from infrastructure.db.wiki_repositories.crud import WikiRepository,Wiki
from infrastructure.db.repositories.super_user_repo import SuperUserRepository
from django.db.models.manager import BaseManager
from django.db.models import Sum,Count

# import pandas as pd
# import numpy as np

class UserRatingService(SuperUserRepository):
    def __init__(self,admin:User):
        super().__init__(admin)
        pass
    
    def get_users(self) -> BaseManager[User]:
        return User.objects.prefetch_related("my_wiki").all()
    
    def sort_users(self,users:BaseManager[User]):
        users_with_likes = users.annotate(total_likes=Count("my_wiki__likes")).distinct().order_by("-total_likes")[:1000]
        user_list = []
        for user in users_with_likes:
            obj = {
                "username":user.username,
                "id":user.id,
                "likes_count":user.total_likes
            }
            # print(user.username,user.total_likes)        
            user_list.append(obj)
        return user_list