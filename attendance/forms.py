from .models import Attendance
from django import forms
from django.forms import widgets

class AttendanceForm(forms.ModelForm):
    # exclude = ['']
    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
                'totalHoursWorked' : forms.TextInput(attrs={'placeholder' : 'HH:MM:SS'})
        }