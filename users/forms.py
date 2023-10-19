from django.forms import ModelForm
from .models import Employee
from django import forms
from django.contrib.auth.forms import UserCreationForm

class EmployeeSignupForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = [ 'first_name', 'last_name', 'email','contact_no','date_of_birth','address', 'gender', 'city', 'state', 'is_manager', 'technology', 'designation', 'year_of_experience', 'joining_date', 'id_proof' , 'id_proof_file']
        exclude = ['']
        # fields = "__all__"


class EmployeeSigninForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'custom-input'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input'}))



class SendMailForm(forms.Form):

    email : forms.EmailField()
    subject : forms.CharField(max_length=200)
    message : forms.Textarea()


class ResetPasswordForm(forms.Form):
    oldPassword  = forms.CharField()
    newPassword  = forms.CharField()


class ChangePasswordForm(forms.Form):
    newPassword = forms.CharField()
    confirmPassword = forms.CharField()

class ForgetPasswordForm(forms.Form):

    email = forms.EmailField()

class UpdateProfileForm(forms.Form):

    class Meta:
        model = Employee
        fields = [ 'first_name', 'last_name', 'email','contact_no','date_of_birth','address', 'gender', 'city', 'state', 'is_manager', 'technology', 'designation', 'year_of_experience', 'joining_date', 'id_proof' , 'id_proof_file']
        exclude = ['']

    





