from .models import Attendance
from django import forms
from django.forms import widgets

class AttendanceForm(forms.ModelForm):
    # exclude = ['']
    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
                'total_working_hours' : forms.TextInput(attrs={'placeholder' : 'HH:MM:SS'})
        }