from celery import shared_task
from django.utils import timezone
from .utils import calculate_gross_salary, calculate_salary_deduction, calculate_net_salary
from .models import SalarySlipGeneration, Employee, Salary
from datetime import datetime

@shared_task
def generate_salary_slip(employee_id):
    employee = Employee.objects.get(id=employee_id)
    salary_instance = Salary.objects.get(employee=employee)
    
    payslip_generation_date = timezone.now()
    gross_salary = calculate_gross_salary(employee_id)
    salary_deduction = calculate_salary_deduction(employee_id)
    net_salary = calculate_net_salary(employee_id)
    
    SalarySlipGeneration.objects.create(
        employee=employee,
        gross_salary=gross_salary,
        salary_deduction=salary_deduction,
        net_salary=net_salary,
        payslip_generation_date=payslip_generation_date
    )