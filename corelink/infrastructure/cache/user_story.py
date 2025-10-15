import redis
from infrastructure.redis_settings import DB,HOST,PORT

class UserStory:
    def __init__(self,user_id):
        self.redis = redis.Redis(HOST,PORT,DB)
        self.data = f"user_story:{user_id}"
        pass
    def SET_DATA(self,wiki_id):
        self.redis.lpush(self.data,wiki_id)
        self.redis.expire(self.data,time=(60*60*24*7))
        return
    def GET_DATA(self):
        data = [i.decode() for i in self.redis.lrange(self.data,0,-1)]
        return data