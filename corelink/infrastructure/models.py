from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    active = models.IntegerField(default=0)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="activity")
    last_active = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"User : {self.user.username} activity : {self.activity}"

class Wiki(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User,models.CASCADE,related_name="my_wiki")
    likes = models.ManyToManyField(User,related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    