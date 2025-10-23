from django.db import models
from infrastructure.models import Wiki

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)
    wikis = models.ManyToManyField(Wiki,related_name="tags")
    
    def __str__(self):
        return self.name