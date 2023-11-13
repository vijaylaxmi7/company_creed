from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from .models import EmployeeLeave
from users.models import Employee


class LeaveApplicationForm(forms.ModelForm):
        
    class Meta:
        model = EmployeeLeave
        fields = ['start_date', 'end_date', 'type', 'leave_choice', 'reason', 'manager']
        labels = {
            'manager' : 'Mail to'
        }

        widgets = {
            'start_date' : SelectDateWidget(),
            'end_date'  : SelectDateWidget()
        }

        exclude = ['employee', 'status']

    
