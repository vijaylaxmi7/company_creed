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

from django.core.mail import EmailMessage, get_connection, send_mail
from django.template import Context, Template, RequestContext

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.


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


class viewTask(ListView):
    model = Task
    exclude_fields = ['description']
    template_name = 'task/view-task.html'




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




class TaskAssignment(View):

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
                description = form.cleaned_data['description']
                employee = form.cleaned_data['employee']
                email_from = settings.EMAIL_HOST_USER
                html = render_to_string('task/taskAssignment.html', 
                                      {'task' : task,
                                       'description' : description
                                        })     
                # message = form.cleaned_data['description']      
                recipient_list = [employee]
                EmailMessage( task,  html,email_from, recipient_list,  connection=connection).send()
            

                form.save()
            # messages.success(request, "Task Assigned!")
            return render('index')
        
        return render(request, self.template_name, {'form' : form})


    

    


    


















    
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
# task_link = request.build_absolute_uri(reverse('task-detail', args = [task.id]))


    
