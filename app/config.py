import os

CELERY_BROKER = os.getenv("CELERY_BROKER", default="redis://127.0.0.1:6379/1")
CELERY_BACKEND = os.getenv("CELERY_BACKEND", default="redis://127.0.0.1:6379/2")
smtp_serv = os.getenv("SMTP_SERVER", default="127.0.0.1")
smtp_port = os.getenv("SMTP_PORT", default=3000)
run_from_docker = os.getenv("CELERY_BROKER", False)
DSN = os.getenv("PG_DSN", default="postgresql://app:1234@127.0.0.1:5431/netology_flask")