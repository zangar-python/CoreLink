from infrastructure.models import Wiki,User
from django.db.models import Count
import redis

from typing import Union
from infrastructure.redis_settings import HOST,PORT,DB

r = redis.Redis(HOST,PORT,DB)

class Cash_To_redis:
    def __init__(self,user:User,data:str="recom"):
        self.data = f"user:{user.id}:{data}"
        pass
    def to_cash(self,wiki_ids):
        r.delete(self.data)
        r.lpush(self.data,*wiki_ids)
        r.expire(self.data,(60*60*1))
        return True
    def get_from_cash(self):
        res =  [ i.decode() for i in r.lrange(self.data,0,-1)]
        return res

class Recom_Wiki:
    def __init__(self,user:User):
        self.user = user
        self.cash = Cash_To_redis(user)
        pass
    def update_cash(self):
        user_likes = Wiki.objects.filter(
            likes__id=self.user.id
        ).values_list(
            "id",flat=True
        )
        our_users = User.objects.filter(
            likes__id__in=user_likes
        ).exclude(
            id-self.user.id,
        ).values_list(
            "id",flat=True
        )
        wikis = Wiki.objects.filter(
            likes__id__in=our_users
        ).exclude(
            id__in=user_likes
        ).distinct().values_list(
            "id"
        )[:100]
        self.cash.to_cash(wikis)
        return
        
    def get_our_like(self):
        result = self.cash.get_from_cash()
        if len(result) == 0:
            print("TO DB!!!")
            user_liked = Wiki.objects.filter(
                likes__id=self.user.id
            ).order_by(
                "-created_at"
            ).values_list(
                "id",
                flat=True
            )
            users_liked_it = User.objects.filter(
                likes__id__in=user_liked
            ).exclude(
                id=self.user.id
            ).values_list(
                "id",flat=True
            )
            res = Wiki.objects.prefetch_related(
                "likes"
            ).filter(
                likes__id__in=users_liked_it
            ).exclude(
                id__in=user_liked
            ).distinct().annotate(
                likes_count=Count("likes")
            ).values(
                "id","likes_count","title","text","author","created_at","updated_at"
            ).order_by("-likes_count")[:100]
            
            ids = [int(i['id']) for i in res]
            self.cash.to_cash(ids)
            return res
        wikis = Wiki.objects.filter(
            id__in=result
        ).annotate(
            likes_count=Count("likes")
        ).order_by(
            "-likes_count"
        ).values(
            "id","likes_count","title","text","author","created_at","updated_at"
        )
        return wikis