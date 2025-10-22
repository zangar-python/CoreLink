from django.dispatch import receiver
from django.db.models.signals import post_migrate
from infrastructure.models import Wiki

from .tasks import update_cash_from_redis

@receiver(post_migrate,sender=Wiki)
def update_recom_cash(sender,instance:Wiki,*kwargs):
    liked_users = instance.likes.all().values_list("id",flat=True)
    update_cash_from_redis.delay(liked_users)