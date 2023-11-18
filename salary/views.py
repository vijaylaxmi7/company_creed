
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from .utils import calculate_net_salary
from django.shortcuts import render
from .models import Salary
from users.models import Employee
from datetime import datetime
from .utils import calculate_gross_salary, calculate_net_salary, calculate_salary_deduction



# Create your views here.

class GenerateSalarySlip(View):

    template_name = 'salary/calculate-salary.html'

    def get(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        salary_instance = Salary.objects.get(employee=employee)
        context = {
            'employee': employee,
            'basic_salary': salary_instance.basic_salary,
            'provident_fund': salary_instance.provident_fund,
            'allowance': salary_instance.allowance,
            'gross_salary': calculate_gross_salary(id),
            'salary_deduction': calculate_salary_deduction(id),
            'net_salary':calculate_net_salary(id) ,
            'salary_period': salary_instance.salary_period,
            'payslip_generation_date': datetime.now(),  
            
        }

        return render(request, self.template_name, context)
    
class EmployeeListView(ListView):
    model = Employee
    template_name = "salary/employee-list.html"





