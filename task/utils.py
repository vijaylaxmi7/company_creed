from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

def send_task_assignment_email(task, employee_email, project, description, start_date, estimate_date, file_attachment):
    subject = "New Task Assignment."
    html_template = get_template('task/task-template.html')
    html_content = html_template.render({
        'task': task,
        'project': project,
        'description': description,
        'start_date': start_date,
        'estimate_date': estimate_date,
        'file_attachment': file_attachment,
    })

    email = EmailMultiAlternatives(
        subject,
        'You have been assigned with a new task.',
        settings.EMAIL_HOST_USER,
        [employee_email],
    )
    email.content_subtype = 'html'
    email.attach_alternative(html_content, 'text/html')
    email.send()