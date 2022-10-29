import os

CELERY_BROKER = os.getenv("CELERY_BROKER", default="redis://127.0.0.1:6379/1")
CELERY_BACKEND = os.getenv("CELERY_BACKEND", default="redis://127.0.0.1:6379/2")
