import celery
import os
from .redis_settings import HOST,PORT,DB
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE","corelink.settings")

celery_app = celery.Celery(
    "corelink",
    backend=f"redis://{HOST}:{PORT}/{DB}",
    broker=f"redis://{HOST}:{PORT}/{DB}",
)

celery_app.autodiscover_tasks(['infrastructure.tasks','analitical_service'])
celery_app.conf.beat_schedule = {
    "top-every-day":{
        "task":"infrastructure.tasks.task.top_wiki_in_a_day",
        "schedule":crontab(hour=0,minute=0)
    },
    "clear-activity-every-day":{
        "task":"infrastructure.tasks.task.active_users_get_delete",
        "schedule":crontab(hour=0,minute=0)
    },
    "top-users-every-hour":{
        "task":"infrastructure.tasks.beat_users_top_by_likes.set_top_users_by_likes",
        "schedule":crontab(hour="*",minute=0)
    },
    "clear-requests-change-every-week":{
        "task":"infrastructure.tasks.beat_clear_request.clear_requests",
        "schedule":crontab(hour=0,minute=0,day_of_week=1)
    },
    
}

# from .tasks.beat_clear_request import clear_requests
# from .tasks.beat_users_top_by_likes import set_top_users_by_likes
# from .tasks.task import create_wiki,active_users_get_delete,top_wiki_in_a_day
# from .tasks.req_to_change_async import set_request_to_change,delete_request_change,accept_request_to_change