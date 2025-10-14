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

# celery_app.autodiscover_tasks(['infrastructure.tasks'])
celery_app.conf.beat_schedules = {
    "top-every-day":{
        "task":"infrastructure.tasks.task.top_wiki_in_a_day",
        "schedule":crontab(hour=0,minute=0)
    },
    "clear-activity-every-day":{
        "task":"infrastructure.tasks.task.active_users_get_delete",
        "schedule":crontab(hour=0,minute=0)
    }
}



from .tasks.task import create_wiki,active_users_get_delete,top_wiki_in_a_day
from .tasks.req_to_change_async import set_request_to_change,delete_request_change,accept_request_to_change