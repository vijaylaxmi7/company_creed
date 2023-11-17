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
            'end_date'  : SelectDateWidget(),
            
        }

        exclude =  ['status']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    
    def clean(self):
            employee = self.request.user.employee
            start_date = self.cleaned_data['start_date']
            end_date = self.cleaned_data['end_date']
            leave_records = EmployeeLeave.objects.filter(employee = employee, start_date = start_date, end_date = end_date)
            if leave_records.exists():
                raise forms.ValidationError("Leave is already applied on these dates.")



            

    
