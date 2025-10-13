from django.contrib.auth.models import User
from ...models import Activity
from typing import Union

class ActivityRepository:
    def __init__(self,user:User):
        self.user = user
        pass
    def set_activity(self):
        Activity.objects.create(user=self.user)
        return True
    def get_activity(self):
        return self.user.activity
    def update(self,ball:Union[int,None]=None):
        if ball:
            self.user.activity.active = self.user.activity.active + ball
        self.user.activity.save()
        return True