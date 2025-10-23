from celery import shared_task
from .service.recom_system import Recom_Wiki
from django.contrib.auth.models import User

@shared_task
def update_cash_from_redis(user_ids):
    users = User.objects.filter(id__in=user_ids)
    for user in users:
        print(user.pk)
        service = Recom_Wiki(user)
        service.update_cash()
        