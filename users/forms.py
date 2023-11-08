from django.forms import ModelForm
from .models import Employee
from django import forms
from django.forms import widgets
from django.forms.widgets import SelectDateWidget, DateInput
from django.contrib.auth.forms import UserCreationForm

class EmployeeSignupForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = [ 'profile_pic','first_name', 'last_name', 'email','contact_no','date_of_birth','address', 'gender', 'city', 'state',   'id_proof' , 'id_proof_file']
        exclude = ['']
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


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email','contact_no','date_of_birth','address', 'gender', 'city', 'state',  'technology',  'id_proof' , 'id_proof_file']
        exclude = ['']

    def _init_(self, *args, **kwargs):
        super(UpdateProfileForm, self)._init_(*args, **kwargs)

    





