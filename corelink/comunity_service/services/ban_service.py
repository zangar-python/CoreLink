import redis
from infrastructure.redis_settings import DB,HOST,PORT
from django.contrib.auth.models import User
from typing import Union

class set_ban_user:
    def __init__(self):
        self.redis = redis.Redis(HOST,PORT,DB)
        pass
    def set_key(self,id_user):
        return f"user:{id_user}:ban"
    def set_ban_to_user(self,user_id,c_id):
        key = self.set_key(user_id)
        self.redis.sadd(key,c_id)
        self.redis.expire(key,(60*60*24)*7)
        return True
    def get_user_bans(self,user_id):
        key = self.set_key(user_id)
        return [int(i.decode()) for i in self.redis.smembers(key)]
    
    def is_user_baned_on(self,user_id,c_id):
        bans = self.get_user_bans(user_id)
        if c_id in bans:
            return True
        return False