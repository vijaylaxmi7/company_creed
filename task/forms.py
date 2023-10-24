from django import forms
from django.forms import ModelForm

from .models import Task
from users.models import Employee



class TaskAssignmentForm(forms.ModelForm):

    # task = forms.CharField(max_length=50)
    # assigned_to = forms.ModelChoiceField(queryset=Employee.objects.all())
    # project = forms.CharField(max_length=50)
    # start_date = forms.DateField()
    # estimate_date = forms.DateField()
    # description = forms.Textarea()
    # attachment = forms.FileField()

    class Meta:
        model = Task
        labels = {
            'employee' : 'Assigned to'
        }
        fields = ['task', 'employee', 'project', 'start_date', 'estimate_date', 'description', 'file_attachment']
        # exlude = ['manager']
        

class EmployeeTaskForm(forms.ModelForm):

    class Meta:

        model = Task
        labels = {
            'employee' : 'Assigned to',
            'manager' : 'Assigned by'
        }
        fields = ['task', 'employee','manager', 'project', 'start_date', 'estimate_date', 'description', 'file_attachment']
        # exlude = ['manager']


    



    




