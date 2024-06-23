import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "p03_online_shop.settings")

app = Celery("p03_online_shop")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.broker_url = "amqp://guest:guest@localhost"
