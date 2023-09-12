import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

celery = Celery('myshop')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()