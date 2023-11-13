from .models import Attendance
from django import forms

class AttendanceForm(forms.ModelForm):
    
    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
                'total_working_hours' : forms.TextInput(attrs={'placeholder' : 'HH:MM:SS'})
        }