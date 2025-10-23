from infrastructure.tasks.task import create_wiki
from django.contrib.auth.models import User
from typing import Union


def start_celery_worker_CREATE_WIKI(user:User,title:str,text:str,tags:list[str]):
    if len(title) > 200:
        return {
            "err":"title length is > 200",
            "ERROR":True
        }
    
    create_wiki.delay(user_id=user.id,title=title,text=text,tags=tags)
    
    
    return {
        "data":"Ваш запрос на создание вики отправлено.Можете перейти на другую страницу",
        "ERROR":False
    }