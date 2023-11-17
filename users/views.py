from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic.edit import UpdateView

from users.forms import EmployeeSignupForm, EmployeeSigninForm
from users.models import Employee

import datetime

# Create your views here.

class EmployeeSignupView(View):

    form = EmployeeSignupForm
    template_name = 'users/employee-signup.html'

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signin/')
        
        return render(request, self.template_name, {'form':form})
    
class EmployeeSigninView(View):

    template_name = 'users/employee-signin.html'
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
    context = {
        'current_datetime': current_datetime,
        'greeting' : greeting}
    
    return render(request, "users/index.html", context)



def Logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect("/signin/")



























    







        
        



        
















