from django.db import models
from users.models import Employee

class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=20, decimal_places=2)
    provident_fund = models.DecimalField(max_digits=20, decimal_places=2)
    allowance = models.DecimalField(max_digits=20, decimal_places=2)
    gross_salary = models.DecimalField(max_digits=20, decimal_places=2)
    net_salary = models.DecimalField(max_digits=20, decimal_places=2)
    salary_deduction = models.DecimalField(max_digits=20, decimal_places=2)
    salary_period = models.CharField(max_length=20)  

class BankAccountDetail(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=60)
    account_no = models.CharField(max_length=30)  
    ifsc_code = models.CharField(max_length=11)
    branch = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    employee_status = models.CharField(max_length=10, default='Active') 

class SalarySlipGeneration(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payslip_generation_date = models.DateTimeField()
    remarks = models.TextField(blank=True)