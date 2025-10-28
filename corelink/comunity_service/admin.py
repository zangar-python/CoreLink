from django.contrib import admin

# Register your models here.
from .models import Comunity,Message

admin.site.register(Comunity)
admin.site.register(Message)