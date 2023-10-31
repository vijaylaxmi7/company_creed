from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget, DateInput
from .models import EmployeeLeave
from users.models import Employee


class leaveApplicationForm(forms.ModelForm):
        
    class Meta:
        model = EmployeeLeave
        fields = ['startDate', 'endDate', 'type', 'leaveChoice', 'reason', 'manager']
        labels = {
            'manager' : 'Mail to'
        }

        widgets = {
            'startDate' : SelectDateWidget(),
            'endDate'  : SelectDateWidget()
        }

        exclude = ['employee', 'status']

    
