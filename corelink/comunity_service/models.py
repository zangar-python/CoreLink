from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comunity(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    users = models.ManyToManyField(User,related_name="comunity")
    admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name="my_comunity")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Message(models.Model):
    comunity = models.ForeignKey(Comunity,on_delete=models.CASCADE,related_name="messages")
    from_user = models.ForeignKey(User,models.CASCADE,related_name="my_messages")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)