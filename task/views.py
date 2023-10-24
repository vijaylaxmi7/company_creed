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
from django.urls import reverse_lazy

from django.core.mail import EmailMessage, get_connection, send_mail
from django.conf import settings

# Create your views here.



class taskDescription(DetailView):
    model = Task


def myTask(request):

    tasks = Task.objects.all().filter(user = request.user)

    return render(request, 'tasks/my-task.html', {'tasks' : tasks})


class updateTask(UpdateView):
    model = Task
    fields = ['task', 'employee', 'project', 'start_date', 'estimate_date', 'description', 'file_attachment']
    template_name = 'task/updateTask.html'
    success_url = reverse_lazy('view-task')
    print("dfghj")
    

class deleteTask(DeleteView):
    model =Task
    template_name = 'task/delete-task.html'
    success_url = reverse_lazy("view-task")
    

# def delete_task(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return render("index")


class TaskAssignment(View):
    
    form = TaskAssignmentForm
    template_name = 'task/taskAssignment.html'

    def get(self, request):

       return render(request, self.template_name, {'form': self.form})
    
    def post(self, request):

        form = TaskAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            # task = form.save(commit=False)
            form.save()
            return HttpResponseRedirect('/index/')
        return render(request, self.template_name, {'form' : form})
    

    

class viewTask(ListView):
    model = Task
    exclude_fields = ['description']
    template_name = 'task/view-task.html'

    
    

# def myTask(request):


#     # current_user = request.user.id

#     # task = Task.objects.all().filter(user = current_user)
#     task = Task.objects.all()

#     context = {'task' : task}

#     return render(request, 'users/index.html', context=context)

# class taskAssignment(View):

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
#                 employee = form.cleaned_data['employee']
#                 email_from = settings.EMAIL_HOST_USER
#                 recipient_list =  [form.cleaned_data('employee')]
#                 manager = form.cleaned_data['manager']
#                 project = form.cleaned_data['project']
#                 start_date = form.cleaned_data['start_date']
#                 estimate_date = form.cleaned_data['estimate_date']
#                 message = form.cleaned_data['description']
#                 file_attachment = form.cleaned_data['file_attachment'] 
#                 recipient_list = [employee]

                
#                 EmailMessage( task, email_from, message, recipient_list,  connection=connection).send()
            

#             # form.save()
#             # messages.success(request, "Task Assigned!")
#             # return render('send-task')
        
#         return render(request, self.template_name, {'form' : form})


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
            message = render_to_string(
        'app/includes/email.html',
        {'pk': site_id}
    )
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

    # return render(request, 'task/taskAssignment.html')

