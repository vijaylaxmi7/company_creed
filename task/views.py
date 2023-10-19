from django.shortcuts import render

from django.views import View
from .forms import TaskAssignmentForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

class taskAssignment(View):

    form = TaskAssignmentForm
    template_name = 'task/taskAssignment.html'

    def get(self, request):

        return render(request, self.template_name, {'form': self.form})
    
    def post(self, request):

        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Assigned!")
            return HttpResponse('success')
        
        return render(request, self.template_name, {'form' : form})


