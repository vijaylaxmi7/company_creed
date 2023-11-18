from django.db import models

# Create your models here.

from users.models import Employee

class EmployeeLeave(models.Model):

    LEAVE_TYPE = [
        ('PAID_LEAVE', 'Paid Leave'),
        ('COMPOFF', 'Compoff'),
        ('OPTIONAL LEAVE', 'Optional Leave'),
        ('CASUAL LEAVE', 'Casual Leave')
      ]

    Leave_Choice = [
      ('Full Day', 'Full Day Leave'),
      ('Half Day', 'Half Day leave')]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="leave_manager", null=True)
    type = models.CharField(max_length=50, choices=LEAVE_TYPE)
    leave_choice = models.CharField(max_length=50, choices=Leave_Choice, default='Full Day')
    status = models.CharField(max_length=50, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ])
    reason = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    



    
    
    

