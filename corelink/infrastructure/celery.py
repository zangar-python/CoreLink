import celery
import os
from .redis_settings import HOST,PORT,DB

os.environ.setdefault("DJANGO_SETTINGS_MODULE","corelink.settings")

celery_app = celery.Celery(
    "corelink",
    backend=f"redis://{HOST}:{PORT}/{DB}",
    broker=f"redis://{HOST}:{PORT}/{DB}",
)

# celery_app.autodiscover_tasks(['infrastructure.tasks'])
from .tasks.task import hello_world
from .tasks.task import create_wiki
