from django.db import models

# Create your models here.

# from users.models import Employee


# class EmployeeLeave(models.Model):

#     LEAVE_TYPE = [
#         ('PAID_LEAVE', 'Paid Leave'),
#         ('COMPOFF', 'Compoff'),
#         ('OPTIONAL LEAVE', 'Optional Leave'),
#         ('CASUAL LEAVE', 'Casual Leave')
#     ]

#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     leave_type = models.CharField(max_length=50, choices=LEAVE_TYPE)
#     reason = models.CharField(max_length=500)
#     leave_start_date = models.DateField()
#     leave_end_date = models.DateField()
    
