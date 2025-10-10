from .User_Profile import UserProfile
from typing import Union
from infrastructure.db.repositories.activity_repo import ActivityRepository


class ActivityEntity(UserProfile):
    def __init__(self, user):
        super().__init__(user)
    
    def set_active(self,ball:Union[int,None]):
        return ActivityRepository(self.user).update(ball)
    
    def get_active(self):
        return ActivityRepository(self.user).get_activity()