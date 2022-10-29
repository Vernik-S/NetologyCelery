import os
import smtplib

from email.mime.text import MIMEText

from celery import Celery
from celery.result import AsyncResult

from config import CELERY_BROKER, CELERY_BACKEND, smtp_serv, smtp_port

celery_app = Celery("app", backend=CELERY_BACKEND, broker=CELERY_BROKER)


def get_task(task_id: str) -> AsyncResult:
    return AsyncResult(task_id, app=celery_app)

@celery_app.task
def send_mail(sender, recipient, msg):

    with smtplib.SMTP(smtp_serv, smtp_port) as server:
        mail = MIMEText(msg)
        mail['Subject'] = "Message about your adv"
        mail['From'] = sender
        mail['To'] = recipient

        server.sendmail(sender, [recipient], mail.as_string())

    return f'Message for {recipient} is sent'

def test_send():

    with smtplib.SMTP(smtp_serv, smtp_port) as server:
        mail = MIMEText("test send")
        mail['Subject'] = "test_send"
        mail['From'] = "test_send"
        mail['To'] = "test_send"

        server.sendmail("test_sender", ["test_reci"], mail.as_string())

    return f'Message for {"test_reci"} is sent'


if __name__ == '__main__':
    test_send()


