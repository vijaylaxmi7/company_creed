from django.db import models
from users.models import Employee

class Salary(models.Model):

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(decimal_places=2, max_digits=20)
    provident_fund = models.DecimalField(decimal_places=2, max_digits=20)
    gross_salary = models.DecimalField(decimal_places=2, max_digits=20)
    net_salary = models.DecimalField(decimal_places=2, max_digits=20)
    
class BankAccountDetail(models.Model):

    employee = models.ForeignKey(Employee, on_delete= models.CASCADE)
    bank_name = models.CharField(max_length=60)
    account_no = models.IntegerField()
    ifsc_code = models.CharField(max_length=11)
    branch = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)

class SalarySlipGeneration(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payslip_generation_date = models.DateTimeField()
    salary_deduction = models.DecimalField(decimal_places=2, max_digits=15)
    



    


    



    
    
