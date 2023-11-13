from django.forms import ModelForm
from .models import Employee
from django import forms
from django.forms import widgets
from django.forms.widgets import SelectDateWidget, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class EmployeeSignupForm(UserCreationForm):

    contact_no = forms.CharField(
        validators=[
            RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit mobile number.'),
        ]
    )

    class Meta:
        model = Employee
        fields = ['profile_pic', 'first_name', 'last_name', 'email','contact_no','date_of_birth','address', 'gender', 'city', 'state',   'id_proof' , 'id_proof_file']
        
        widgets = {
            'date_of_birth' : DateInput(attrs={'type': 'date'}),
        }
        

        
class EmployeeSigninForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'custom-input'}))
    password = forms.CharField(widget=forms.PasswordInput)



class SendMailForm(forms.Form):

    email : forms.EmailField()
    subject : forms.CharField(max_length=200)
    message : forms.Textarea()



    





