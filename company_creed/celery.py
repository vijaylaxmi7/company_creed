# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "company_creed.settings")
app = Celery("company_creed")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'generate-salary-slips': {
        'task': 'salary.tasks.generate_salary_slip',
        'schedule': crontab(day_of_month=5, hour=0, minute=0),
    },
}