import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News.settings')

app = Celery('News')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'newsportal.tasks.my_job',
        'schedule': 30,
        # 'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}