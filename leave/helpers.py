from django.core.mail import send_mail
import uuid
from django.conf import settings

def send_leave_apply(email, token, task):
    subject = 'New Task Assigned'
    message = f'Hi, click on the link to see new task http://127.0.0.1:8000/my-task/{task}/{token}/ '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True