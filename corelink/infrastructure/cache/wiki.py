import redis
from infrastructure import redis_settings

r = redis.Redis(
    host=redis_settings.HOST,port=redis_settings.PORT,db=redis_settings.DB
)

class Redis_Wiki:
    def __init__(self):
        pass
    
    def set_sadd(self,name,values):
        r.sadd(name,*values)
        return True
    def get_smembers(self,name):
        return [i.decode() for i in r.smembers(name)]
    def delete(self,names):
        r.delete(names)