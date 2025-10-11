from celery import shared_task


@shared_task
def hello_world():
    print("hello world")

@shared_task
def create_wiki(user_id,title,text):
    from django.contrib.auth.models import User
    from domain.services.wiki_service.wiki_crud_service import WikiService    
    if not User.objects.filter(id=user_id).exists():
        return "User is not exists"
    user = User.objects.get(id=user_id)
    wiki_service = WikiService(user=user)
    wiki_service.set_wiki(title=title,text=text)
    return "Created"