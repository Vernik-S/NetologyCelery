import smtplib

from email.mime.text import MIMEText


def send_mail(sender, recipient, msg, server):
    mail = MIMEText(msg)
    mail['Subject'] = "Message about your adv"
    mail['From'] = sender
    mail['To'] = recipient

    server.sendmail(sender, [recipient], mail.as_string())

    return f'Message for {recipient} is sent'

def test_send():
    with smtplib.SMTP('127.0.0.1', 3000) as server:
        print(send_mail("send@send.aa", "receiver@receive.aa", "test_message", server))





