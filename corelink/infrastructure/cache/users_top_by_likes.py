import redis
from infrastructure.redis_settings import HOST,PORT,DB

class UserTop_toCache:
    def __init__(self):
        self.users_id = "users_id"
        self.users_data = "users"
        self.redis = redis.Redis(HOST,PORT,DB)
        pass
    def SET_DATA(self,users):
        self.clear_data()
        self.redis.sadd(self.users_id,*[i['id'] for i in users])
        self.set_h_data(users)
        return 
    
    def clear_data(self):
        self.redis.delete(self.users_id)
        self.redis.delete(f"self.users_data:*")
        return
    
    def set_h_data(self,users):
        for user in users:
            self.redis.hset(f"{self.users_data}:{user['id']}",mapping=user)
        return
    
    def GET_DATA(self):
        users_id = [i.decode() for i in self.redis.smembers(self.users_id)]
        return self.get_h_data(users_id)
        
    def get_h_data(self,users_id):
        users = []

        for id in users_id:
            user = self.decode_h_data(self.redis.hgetall(f"{self.users_data}:{id}"))
            users.append(user)
        return users
    
    
    def decode_h_data(self,data):
        return {i.decode():k.decode() for i,k in data.items()}