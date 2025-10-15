from celery import shared_task


@shared_task
def clear_requests():
    from datetime import timedelta
    from django.utils import timezone
    from infrastructure.models import Request_To_Change_Wiki
    Request_To_Change_Wiki.objects.filter(created_at__gte=timezone.now()-timedelta(days=7)).delete()
    return