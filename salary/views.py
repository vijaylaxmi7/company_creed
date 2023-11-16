
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from .models import Salary
from users.models import Employee
from attendance.models import Attendance, TotalWorkingHours
from datetime import datetime


# Create your views here.

class CalculateSalary(View):

    template_name = 'templates/calculate-salary.html'

    def post(request):

        employee = Employee.objects.all()
        

        





