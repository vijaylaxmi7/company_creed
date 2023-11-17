
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from .models import Salary
from django.http import HttpResponseNotAllowed
from users.models import Employee
from attendance.models import Attendance, TotalWorkingHours
from datetime import datetime
from attendance.utils import calculate_total_working_hours
from decimal import Decimal


# Create your views here.

class CalculateSalary(View):
    template_name = 'salary/calculate-salary.html'

    def get(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        salary_instance = Salary.objects.get(employee=employee)
        hourly_rate = salary_instance.basic_salary / 8
        total_working_hours = calculate_total_working_hours(id)
        total_working_hours_numeric = Decimal (total_working_hours.total_seconds()) / Decimal(3600)
        salary_instance.net_salary = total_working_hours_numeric * hourly_rate
        salary_instance.save()

        context = {
            'employee': employee,
            'basic_salary': salary_instance.basic_salary,
            'provident_fund': salary_instance.provident_fund,
            'allowance': salary_instance.allowance,
            'gross_salary': salary_instance.gross_salary,
            'net_salary': salary_instance.net_salary,
            'salary_deduction': salary_instance.salary_deduction,
            'salary_period': salary_instance.salary_period,
            'payslip_generation_date': datetime.now(),  
            
        }

        return render(request, self.template_name, context)
    
class EmployeeListView(ListView):
    model = Employee
    template_name = "salary/employee-list.html"





