from .models import Salary, SalarySlipGeneration
from attendance.utils import calculate_total_working_hours
from django.shortcuts import get_object_or_404
from users.models import Employee
from decimal import Decimal

def calculate_gross_salary(id):
    employee = get_object_or_404(Employee, id = id)
    salary_instance = Salary.objects.get(employee=employee)
    hourly_rate = salary_instance.basic_salary / 152
    total_working_hours = calculate_total_working_hours(id)
    total_working_hours_numeric = Decimal (total_working_hours.total_seconds()) / Decimal(3600)
    calculated_monthly_salary = round(total_working_hours_numeric * hourly_rate, 2)
    gross_salary = calculated_monthly_salary  +  salary_instance.allowance
    salary_slip = SalarySlipGeneration(employee=employee, gross_salary = gross_salary)
    salary_slip.save()
    return gross_salary

def calculate_salary_deduction(id):
    salary_instance = Salary.objects.get(employee=id)
    salary_slip = SalarySlipGeneration.objects.filter(employee=id).first()
    if salary_slip:
        salary_slip.salary_deduction =  salary_instance.provident_fund + salary_instance.tax_rate
        
        salary_deduction = salary_slip.salary_deduction
        salary_slip.save()
        print(salary_slip.salary_deduction)
        return salary_deduction
    else:
        return 0

def calculate_net_salary(id):
    salary_slip = SalarySlipGeneration.objects.filter(employee=id).first()
    gross_salary = calculate_gross_salary(id)
    salary_deduction = calculate_salary_deduction(id)
    
    if salary_slip:
        salary_slip.net_salary = gross_salary - salary_deduction
        print(salary_slip.net_salary)
        salary_slip.save()
        return salary_slip.net_salary
    else:
        return 0  