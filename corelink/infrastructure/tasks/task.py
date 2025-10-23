from celery import shared_task


@shared_task
def hello_world():
    print("hello world")

@shared_task
def create_wiki(user_id,title,text,tags):
    from django.contrib.auth.models import User
    from domain.services.wiki_service.wiki_crud_service import WikiService 
    
    if not User.objects.filter(id=user_id).exists():
        return "User is not exists"
    user = User.objects.get(id=user_id)
    wiki_service = WikiService(user=user)
    res = wiki_service.set_wiki(title=title,text=text,tags=tags)
    
    return res

@shared_task
def active_users_get_delete():
    from django.contrib.auth.models import User
    
    users = User.objects.select_related("activity").all()
    for user in users:
        user.activity.active = 0
        user.activity.save
    return "Active = 0"
    
@shared_task 
def top_wiki_in_a_day():
    from domain.services.wiki_service.wiki_crud_service import WikiService
    from django.contrib.auth.models import User
    from infrastructure import redis_settings
    
    
    admin = User.objects.filter(is_superuser=True).first()
    if not admin:
        admin = User.objects.create(
            username=redis_settings.ADMIN_USERNAME,
            password=redis_settings.ADMIN_PASSWORD,
            email=redis_settings.ADMIN_EMAIL,
        )
        admin.is_superuser = True
        admin.save()
    wikis_id = [i.id for i in WikiService(admin).top_wikis_in_a_day()]
    repo = Top_Wikis()
    repo.set(wikis_id)

class Top_Wikis:
    from infrastructure.cache.wiki import Redis_Wiki
    name = "top"
    def __init__(self):
        pass
    def get(self):
        return self.Redis_Wiki().get_smembers(name=self.name)
    def set(self,values):
        return self.Redis_Wiki().set_sadd(name=self.name,values=values)
    def delete(self):
        return self.Redis_Wiki().delete(self.name)