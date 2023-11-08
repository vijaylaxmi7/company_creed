from django.shortcuts import render

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .forms import TaskAssignmentForm, SendTaskStatusForm
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
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render , get_object_or_404

# Create your views here.


def TaskStatus(request):
     
    if request.method == 'POST':
        task_status = get_object_or_404(Task, id=id)
        print(task_status)
        action = request.POST.get('action', '')
        if action == 'Completed':
            task_status.status = 'Completed'
            task_status.save()
            return HttpResponseRedirect('/leave/manage-leave/')
        elif action == 'reject':
            task_status.status = 'Rejected'
            task_status.save()
            return HttpResponseRedirect('/leave/manage-leave/')

    return render(request, 'leave/manage-leave.html')




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


class SendTaskStatus(View):
     
     template_name = 'task/task-status.html'
     form = SendTaskStatusForm

     def get(self,request):

        return render(request, self.template_name, {'form': self.form})
     
     def post(self, request):
          
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/task/my-task/')
        
        return render(request, self.template_name, {'form':form})
    


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

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'  

def myTask(request):

    task = Task.objects.filter(employee = request.user.employee)
    context = {'task' : task}
    return render(request, 'task/my-task.html', context=context)

    
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


    

    


    

































    
