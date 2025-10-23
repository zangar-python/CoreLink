from django.contrib import admin
from .models import Tag

from infrastructure.models import Wiki,User,Message,Request_To_Change_Wiki,Activity
# Register your models here.
admin.site.register(Tag)
admin.site.register(Wiki)
admin.site.register(Message)
admin.site.register(Request_To_Change_Wiki)
admin.site.register(Activity)
# admin.site.register()