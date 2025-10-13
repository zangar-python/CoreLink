from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    active = models.IntegerField(default=0)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="activity")
    last_active = models.DateTimeField(auto_now=True)
    redacting = models.BooleanField(default=True)
    
    def __str__(self):
        return f"User : {self.user.username} activity : {self.activity}"

class Wiki(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User,models.CASCADE,related_name="my_wiki")
    likes = models.ManyToManyField(User,related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    from_user = models.ForeignKey(User,models.CASCADE,related_name="my_messages")
    to_user = models.ForeignKey(User,models.CASCADE,related_name="messages")
    text = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

class Request_To_Change_Wiki(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    wiki = models.ForeignKey(Wiki,on_delete=models.CASCADE,related_name="requests_to_change")
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="my_requests_to_change")
    to_author = models.ForeignKey(User,models.CASCADE,related_name="requests_to_change")