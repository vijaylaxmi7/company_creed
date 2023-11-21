from django.db import models
from users.models import Employee
from django.utils import timezone

class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=20, decimal_places=2)
    hra = models.DecimalField(max_digits=20, decimal_places=2)
    provident_fund = models.DecimalField(max_digits=20, decimal_places=2)
    allowance = models.DecimalField(max_digits=20, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)


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
    gross_salary = models.DecimalField(max_digits=20, decimal_places=2)
    net_salary = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    salary_deduction = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    payslip_generation_date = models.DateTimeField(default=timezone.now)
    stripe_payment_intent = models.CharField(max_length=200, default= False)
    paid = models.BooleanField(default=False, verbose_name='Payment Status')

   