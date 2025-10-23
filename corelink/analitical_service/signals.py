from django.dispatch import receiver
from django.db.models.signals import post_migrate
from infrastructure.models import Wiki

from .tasks import update_cash_from_redis

@receiver(post_migrate,sender=Wiki)
def update_recom_cash(sender,instance:Wiki,**kwargs):
    liked_users_id = [i.pk for i in instance.likes.all()]
    update_cash_from_redis.delay(liked_users_id)