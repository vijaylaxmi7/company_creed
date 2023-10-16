from typing import Any
from django.http import HttpRequest, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView
from users.forms import EmployeeSignupForm, EmployeeSigninForm, ResetPasswordForm, ForgetPasswordForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.core.mail import EmailMessage, get_connection, send_mail
from django.contrib.auth import update_session_auth_hash
import uuid
from django.conf import settings
from .helpers import send_forget_password_mail
from django.contrib.auth import get_user_model
User = get_user_model



# Create your views here.


class EmployeeSignupForm(View):

    form = EmployeeSignupForm
    template_name = 'users/EmployeeSignup.html'

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup Successful!")
        
        return render(request, self.template_name, {'form':form})
    

class EmployeeSignin(View):

    template_name = 'users/EmployeeSignin.html'
    form = EmployeeSigninForm
    
    def get(self, request):
        form = self.form()
        return render(request, self.template_name, context={'form': form})
        
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, "Signin Successful!")
                return HttpResponse("signedin")
            
            return render(request, self.template_name, context={'form': form})
                
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})
    


# def success(self):
#         messages.success(self.request, 'logged in')
#         return reverse('EmployeeSignin')
    

def Logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponse("logged out")


def SendMail(request):

    if request.method == 'POST':
        with get_connection(
            host = settings.EMAIL_HOST,
            port = settings.EMAIL_PORT,
            username = settings.EMAIL_HOST_USER,
            password = settings.EMAIL_HOST_PASSWORD,
            use_tls = settings.EMAIL_USE_TLS

        )as connection:
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("email"),]
            message = request.POST.get("message")
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

    return render(request, 'users/sendMail.html')



class resetPasswordView(View):

    form = ResetPasswordForm
    template_name = 'users/reset_password.html'

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, context={'form': form})
    
    def post(self, request):
        
        if request.method == 'POST':
            form = self.form(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

        return render(request, self.template_name, {'form': form})


def changePassword(request, token):
    form = ChangePasswordForm
    obj = User.objects.get(token)
    return render(request, 'users/change_password.html', context={'form': form})


def ForgetPassword(request):

    form = ForgetPasswordForm

    if request.method == 'POST':
            form = form(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']

            if not User.objects.filter(email = email).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget-password/')
            
            user_obj = User.objects.get(email = email)
            token = str(uuid.uuid4())

            send_forget_password_mail(user_obj, token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget-password/')
    return render(request, 'users/forget_password.html', context={'form': form})




        
        



        

















   
