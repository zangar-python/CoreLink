from infrastructure.models import Wiki,User
from django.db.models import Count
from django.db.models.manager import BaseManager
# from tag_service.services.repo_tag import Tag_Wiki_Repo
import redis

from typing import Union
from infrastructure.redis_settings import HOST,PORT,DB

r = redis.Redis(HOST,PORT,DB)

class Cash_To_redis:
    def __init__(self,user:User,data:str="recom"):
        self.data = f"user:{user.id}:{data}"
        pass
    def to_cash(self,wiki_ids):
        if not wiki_ids:
            return False
        r.delete(self.data)
        print(type(wiki_ids),wiki_ids)
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
            id=self.user.id,
        ).values_list(
            "id",flat=True
        )
        wikis = Wiki.objects.filter(
            likes__id__in=our_users
        ).exclude(
            id__in=user_likes
        ).distinct()[:100]
        self.cash.to_cash([i.pk for i in wikis])
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
class Recom_By_Tag:
    def __init__(self,user:User):
        self.user = user
        self.cash = Cash_To_redis(user,data="by_tag")
        pass
    
    def get_recomend(self):
        user_liked_wikis : BaseManager = self.user.likes.all()
        tags_id = user_liked_wikis.values_list("tags__id",flat=True)
        wikis_with_this_tags = Wiki.objects.filter(
            tags__id__in=tags_id
        ).distinct().order_by("-created_at")[:100]
        return wikis_with_this_tags
    
    def get_from_cash(self):
        return self.cash.get_from_cash()
    def set_to_cash(self,wikis:BaseManager[Wiki]):
        rec_ids = [i.id for i in wikis]
        return self.cash.to_cash(rec_ids)
    
    def GET(self):
        ids = self.get_from_cash()
        if len(ids) == 0:
            wikis = self.get_recomend()
            self.set_to_cash(wikis)
            return wikis
        else:
            wikis = Wiki.objects.filter(id__in=ids).order_by("-created_at")[:100]
            return wikis
    def SET(self):
        wikis = self.get_recomend()
        return self.set_to_cash(wikis)