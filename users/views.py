from typing import Any
from django.http import HttpRequest, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from users.forms import EmployeeSignupForm, EmployeeSigninForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
User = get_user_model

from users.models import Employee, CustomUser
from django.views.generic.edit import UpdateView
from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy
import datetime
from django.utils import timezone


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
            return HttpResponseRedirect('/signin/')
        
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
                # messages.success(request, "Signin Successful!")
                return HttpResponseRedirect('/index/')
            else :
                return HttpResponse("not authenticate")
                
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


class EditProfileView(UpdateView):

    model = Employee
    fields = [ 'first_name', 'last_name', 'email','contact_no','date_of_birth','address', 'gender', 'city', 'state','id_proof' , 'id_proof_file']
    template_name ="users/edit_profile.html"
    success_url = reverse_lazy('index')

    def id(self):
        return self.request.user.id
    

def index(request):
    
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    current_datetime = timezone.now().strftime("%I:%M%p on %B %d, %Y")
    # current_datetime = timezone.localtime()
    context = {
        'current_datetime': current_datetime,
        'greeting' : greeting}
    return render(request, "users/index.html", context)



def Logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect("/signin/")
























# class resetPasswordView(View):

#     form = ResetPasswordForm
#     template_name = 'users/reset_password.html'

#     def get(self, request):
#         form = self.form()
#         return render(request, self.template_name, context={'form': form})
    
#     def post(self, request):
        
#         if request.method == 'POST':
#             form = self.form(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')

#         return render(request, self.template_name, {'form': form})


# def changePassword(request, token):
#     form = ChangePasswordForm
#     obj = User.objects.get(token)
#     return render(request, 'users/change_password.html', context={'form': form})


# def ForgetPassword(request):

#     form = ForgetPasswordForm
#     print('hi')

#     if request.method == 'POST':
#             form = form(request.POST)
#             if form.is_valid():
#                 email = form.cleaned_data['email']

#                 if not User.objects.filter(email = email).first():
#                     messages.success(request, 'Not user found with this username.')
#                     return redirect('/forget-password/')
                
#                 user_obj = User.objects.get(email = email)
#                 token = str(uuid.uuid4())

#                 send_forget_password_mail(user_obj, token)
#                 messages.success(request, 'An email is sent.')
#                 return redirect('/forget-password/')
#     return render(request, 'users/forget_password.html', context={'form': form})





# def ForgetPassword(request):

#     form = ForgetPasswordForm


#     if request.method == 'POST':
#             form = form(request.POST)
#             if form.is_valid():
#                 data = form.cleaned_data['email']
#                 associated_users = User.objects.filter(Q(email=data))

#                 if not associated_users.exists():
#                     messages.success(request, 'Not user found with this username.')
#                     return redirect('/forget-password/')
                
#                 user_obj = User.objects.get(email = data)
#                 token = str(uuid.uuid4())

#                 send_forget_password_mail(user_obj, token)
#                 messages.success(request, 'An email is sent.')
#                 return redirect('/forget-password/')
#     return render(request, 'users/forget_password.html', context={'form': form})






# class EditProfile(View):

#     def get(self, request):



    







        
        



        
















