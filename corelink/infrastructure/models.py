from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    active = models.IntegerField(default=0)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="activity")
    last_active = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"User : {self.user.username} activity : {self.activity}"