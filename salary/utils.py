from .models import Salary, SalarySlipGeneration
from attendance.utils import calculate_total_working_hours
from django.shortcuts import get_object_or_404
from users.models import Employee
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import datetime

from decimal import Decimal


def send_salary_slip(id):
    employee = get_object_or_404(Employee, id = id)
    salary_instance = Salary.objects.get(employee=employee)
    subject = "Salary Slip"
    html_template = get_template('salary/salary-slip-template.html')
    html_content = html_template.render({'employee': employee,
            'basic_salary': salary_instance.basic_salary,
            'provident_fund': salary_instance.provident_fund,
            'allowance': salary_instance.allowance,
            'gross_salary': calculate_gross_salary(id),
            'salary_deduction': calculate_salary_deduction(id),
            'net_salary':calculate_net_salary(id) ,
            'payslip_generation_date': datetime.now(),})
    email = EmailMultiAlternatives(
            subject,
            'You have been assigned with new task.',
            settings.EMAIL_HOST_USER,
            [employee.email],
        )
    email.content_subtype = 'html_template'

    email.attach_alternative(html_content, 'text/html')
    email.send()     

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
        return salary_deduction
   

def calculate_net_salary(id):
    salary_slip = SalarySlipGeneration.objects.filter(employee=id).first()
    gross_salary = calculate_gross_salary(id)
    salary_deduction = calculate_salary_deduction(id)
    
    if salary_slip:
        salary_slip.net_salary = gross_salary - salary_deduction
        salary_slip.save()
        return salary_slip.net_salary
    else:
        return 0  