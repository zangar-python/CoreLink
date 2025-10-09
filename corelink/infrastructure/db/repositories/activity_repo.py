from django.contrib.auth.models import User
from ..models.activity import Activity


class ActivityRepository:
    def __init__(self,user:User):
        self.user = user
        pass
    def set_activity(self):
        activity = Activity.objects.create(user=self.user)
        return True
    def get_activity(self):
        return self.user.activity
    