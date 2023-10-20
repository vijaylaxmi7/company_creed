from django.shortcuts import render

from django.views import View
from .forms import TaskAssignmentForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

from django.core.mail import EmailMessage, get_connection, send_mail
from django.conf import settings

# Create your views here.

class taskAssignment(View):

    form = TaskAssignmentForm
    template_name = 'task/taskAssignment.html'

    def get(self, request):

        return render(request, self.template_name, {'form': self.form})
    
    def post(self, request):

        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            with get_connection(
            host = settings.EMAIL_HOST,
            port = settings.EMAIL_PORT,
            username = settings.EMAIL_HOST_USER,
            password = settings.EMAIL_HOST_PASSWORD,
            use_tls = settings.EMAIL_USE_TLS

        )as connection:
                task = form.cleaned_data['task']
                employee = form.cleaned_data['employee']
                email_from = settings.EMAIL_HOST_USER
                recipient_list =  [form.cleaned_data('employee')]
                manager = form.cleaned_data['manager']
                project = form.cleaned_data['project']
                start_date = form.cleaned_data['start_date']
                estimate_date = form.cleaned_data['estimate_date']
                message = form.cleaned_data['description']
                file_attachment = form.cleaned_data['file_attachment'] 
                recipient_list = [employee]

                
                EmailMessage( task, email_from, message, recipient_list,  connection=connection).send()
            

            # form.save()
            # messages.success(request, "Task Assigned!")
            # return render('send-task')
        
        return render(request, self.template_name, {'form' : form})


def SendTask(request):

    if request.method == 'POST':
        with get_connection(
            host = settings.EMAIL_HOST,
            port = settings.EMAIL_PORT,
            username = settings.EMAIL_HOST_USER,
            password = settings.EMAIL_HOST_PASSWORD,
            use_tls = settings.EMAIL_USE_TLS

        )as connection:
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("email"),]
            message = request.POST.get("message")
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

    # return render(request, 'task/taskAssignment.html')

