from django import forms
from django.forms import ModelForm

from .models import Task
from users.models import Employee
from django.forms.widgets import SelectDateWidget, DateInput


class TaskAssignmentForm(forms.ModelForm):

    class Meta:
        model = Task
        labels = {
            'employee' : 'Assigned to'
        }
        fields = ['task', 'employee', 'project', 'start_date','estimate_date', 'description', 'file_attachment']
        # exlude = ['manager']
        widgets = {
            'start_date' : SelectDateWidget(),
            'estimate_date'  : SelectDateWidget()
        }
        

class SendTaskStatusForm(forms.ModelForm): 
    
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['employee','start_date','estimate_date','file_attachment']
        task = forms.IntegerField(
        widget=forms.Select(
        choices=Task.objects.all().values_list('id', 'task')
        )
     )


class EmployeeTaskForm(forms.ModelForm):

    class Meta:

        model = Task
        labels = {
            'employee' : 'Assigned to',
            'manager' : 'Assigned by'
        }
        fields = ['task', 'employee','manager', 'project', 'start_date', 'estimate_date', 'description', 'file_attachment']
        # exlude = ['manager']


    



    




