from django.core.mail import send_mail
import uuid
from django.conf import settings

def send_task_email(email, token, task):
    subject = 'New Task Assigned'
    message = f'Hi, click on the link to see new task http://127.0.0.1:8000/my-task/{task}/{token}/ '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True


def send_leave_email(email, token, type):
    subject = 'Application for leave'
    message = f'Hi, click on the link to see new task http://127.0.0.1:8000/leave-apply/{type}/{token}/ '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True



    # '7817a612-9ec8-4bb4-939b-3844d555956a'


