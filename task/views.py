from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.conf import settings
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import TaskAssignmentForm
from django.http import HttpResponseRedirect
from .models import Task
from django.core.mail import EmailMultiAlternatives

# Create your views here.

class TaskAssignmentView(View):

    form = TaskAssignmentForm
    template_name = 'task/task-assignment.html'

    def get(self, request):

        return render(request, self.template_name, {'form': self.form})
        
    def post(self, request):

        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.instance.employee = request.user.employee
            task = form.cleaned_data['task']
            email = form.cleaned_data['employee']  
            project = form.cleaned_data['project']
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            estimate_date = form.cleaned_data['estimate_date']
            file_attachment = form.cleaned_data['file_attachment']
            subject = "New Task Assignment."
            html_template = get_template('task/task-template.html')
            html_content = html_template.render({'task':task,'project': project ,'description' : description,'start_date': start_date, 'estimate_date': estimate_date,'file_attachment' : file_attachment})
            email = EmailMultiAlternatives(
                    subject,
                    'You have been assigned with new task.',
                    settings.EMAIL_HOST_USER,
                    [email],
                )
            email.content_subtype = 'html'
            email.attach_alternative(html_content, 'text/html')
            email.send()         
            form.save()
            return HttpResponseRedirect('/index/')
        
        return render(request, self.template_name, {'form' : form})

class UpdateTaskView(UpdateView):
    model = Task
    fields = ['task', 'employee', 'project', 'start_date', 'estimate_date', 'description', 'file_attachment']
    template_name = 'task/update-task.html'
    success_url = reverse_lazy('view-task')
    
class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'task/delete-task.html'
    success_url = reverse_lazy("view-task")

class ListTaskView(ListView):
    model = Task
    exclude_fields = ['description']
    template_name = 'task/view-task.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'  

def my_task(request):

    task = Task.objects.filter(employee = request.user.employee)
    context = {'task' : task}
    return render(request, 'task/my-task.html', context=context)

class UpdateTaskStatusView(UpdateView):

    model = Task
    fields = ['manager', 'task', 'project', 'description','status']
    exclude = ['employee','start_date','estimate_date','file_attachment']
    template_name ="task/task-status.html"
    success_url = reverse_lazy('my-task')

    


    

    


    

































    
