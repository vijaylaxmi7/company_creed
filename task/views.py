from django.shortcuts import render

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .forms import TaskAssignmentForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, request
from .models import Task
from users.models import Employee, CustomUser
from users.views import index
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from django.core.mail import EmailMessage, get_connection, send_mail
from django.template import Context, Template, RequestContext

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import uuid

from users.helpers import send_task_email
from users.helpers import send_leave_email

from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

# Create your views here.



class TaskAssignment(View):

    form = TaskAssignmentForm
    template_name = 'task/taskAssignment.html'

    def get(self, request):

        return render(request, self.template_name, {'form': self.form})
        
    def post(self, request):

        form = self.form(request.POST, request.FILES)
        if form.is_valid():
                    task = form.cleaned_data['task']
                    email = form.cleaned_data['employee']  
                    project = form.cleaned_data['project']
                    description = form.cleaned_data['description']
                    start_date = form.cleaned_data['start_date']
                    estimate_date = form.cleaned_data['estimate_date']
                    file_attachment = form.cleaned_data['file_attachment']
                    subject = "New Task Assignment."
                    html_template = get_template('task/taskTemplate.html')
                    html_content = html_template.render({'task':task,'project': project ,'description' : description,'start_date': start_date, 'estimate_date': estimate_date,'file_attachment' : file_attachment})
                    email = EmailMultiAlternatives(
                            subject,
                            'You have been assigned with new task.',
                            settings.EMAIL_HOST_USER,
                            [email],
                        )
                    email.content_subtype = 'html'
                    # email.attach_alternative(html_content, 'file_attachment')
                    email.send()         
                    form.save()
                    # messages.success(request, "Task Assigned!")
                    return HttpResponseRedirect('/index/')
        
        return render(request, self.template_name, {'form' : form})




class updateTask(UpdateView):
    model = Task
    fields = ['task', 'employee', 'project', 'start_date', 'estimate_date', 'description', 'file_attachment']
    template_name = 'task/updateTask.html'
    success_url = reverse_lazy('view-task')
    
    

class deleteTask(DeleteView):
    model =Task
    template_name = 'task/delete-task.html'
    success_url = reverse_lazy("view-task")


class viewTask(ListView):
    model = Task
    exclude_fields = ['description']
    template_name = 'task/view-task.html'



# class TaskAssignment(View):

#     form = TaskAssignmentForm
#     template_name = 'task/taskAssignment.html'

#     def get(self, request):

#         return render(request, self.template_name, {'form': self.form})
        
#     def post(self, request):

#         form = self.form(request.POST, request.FILES)
#         if form.is_valid():

#             if request.user.employee.is_manager:
#                 with get_connection(
#                 host = settings.EMAIL_HOST,
#                 port = settings.EMAIL_PORT,
#                 username = settings.EMAIL_HOST_USER,
#                 password = settings.EMAIL_HOST_PASSWORD,
#                 use_tls = settings.EMAIL_USE_TLS

#                 )as connection:

#                     task = form.cleaned_data['task']
#                     email = form.cleaned_data['employee']            
#                     token = str(uuid.uuid4())
#                     form.save()
#                     send_task_email(email, token, task)
#                 # messages.success(request, "Task Assigned!")
#                 return HttpResponseRedirect('/index/')
        
#         return render(request, self.template_name, {'form' : form})


    

    


    































# class TaskAssignment(View):
    
#     form = TaskAssignmentForm
#     template_name = 'task/taskAssignment.html'

#     def get(self, request):

#        return render(request, self.template_name, {'form': self.form})
    
#     def post(self, request):

#         form = TaskAssignmentForm(request.POST, request.FILES)
#         if form.is_valid():
#             # task = form.save(commit=False)
#             form.save()
#             return HttpResponseRedirect('/index/')
#         return render(request, self.template_name, {'form' : form})




    
# def SendTask(request):

#     if request.method == 'POST':
#         with get_connection(
#             host = settings.EMAIL_HOST,
#             port = settings.EMAIL_PORT,
#             username = settings.EMAIL_HOST_USER,
#             password = settings.EMAIL_HOST_PASSWORD,
#             use_tls = settings.EMAIL_USE_TLS

#         )as connection:
#             subject = request.POST.get("subject")
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = [request.POST.get("email"),]
#             message = render_to_string('task/taskAssignment.html', 
# #                                        {'name' : name, 
# #                                         'email' : email, 
# #                                         'description' : description})
#     )
#             EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

#     return render(request, 'task/taskAssignment.html')










# def delete_task(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return render("index")




# class TaskAssignment(View):

#     form = TaskAssignmentForm
#     template_name = 'task/taskAssignment.html'

#     def get(self, request):

#         return render(request, self.template_name, {'form': self.form})
    
#     def post(self, request):

#         form = self.form(request.POST, request.FILES)
#         if form.is_valid():
#             with get_connection(
#             host = settings.EMAIL_HOST,
#             port = settings.EMAIL_PORT,
#             username = settings.EMAIL_HOST_USER,
#             password = settings.EMAIL_HOST_PASSWORD,
#             use_tls = settings.EMAIL_USE_TLS

#         )as connection:
#                 task = form.cleaned_data['task']
#                 description = form.cleaned_data['description']
#                 employee = form.cleaned_data['employee']
#                 email_from = settings.EMAIL_HOST_USER
#                 html = render_to_string('task/taskAssignment.html', 
#                                       {'task' : task,
#                                        'description' : description
#                                         })     
#                 # message = form.cleaned_data['description']      
#                 recipient_list = [employee]
#                 EmailMessage( task,  html,email_from, recipient_list,  connection=connection).send()
            

#                 form.save()
#             # messages.success(request, "Task Assigned!")
#             # return render('send-task')
        
#         return render(request, self.template_name, {'form' : form})



# class TaskAssignment(View):
    
#     form = TaskAssignmentForm
#     template_name = 'task/taskAssignment.html'

#     def get(self, request):

#        return render(request, self.template_name, {'form': self.form})
    
#     def post(self, request):

#         form = TaskAssignmentForm(request.POST, request.FILES)
#         if form.is_valid():
#             name = form.cleaned_data['first_name']
#             email = form.cleaned_data['employee']
#             description = form.cleaned_data['description']
#             recipient_list = [email]
#             message = render_to_string('task/taskAssignment.html', 
#                                        {'name' : name, 
#                                         'email' : email, 
#                                         'description' : description})
#             email = EmailMessage("New Task Assignment", message, recipient_list,context_instance=RequestContext(request))
#             return HttpResponseRedirect('/index/')
#         return render(request, self.template_name, {'form' : form})



    
