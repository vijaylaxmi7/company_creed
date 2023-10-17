from django.db import models

 # Create your models here.

from users.models import Employee

class Task(models.Model):


    TASK_STATUS = [
        ('COMPLETED', 'Completed'),
        ('PROCESSING','Processing' ),
        ('HOLD', 'Hold'),
        ('TESTING', 'Testing'),
        ('DEPLOYED', 'Deployed')
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='manager')
    task_name = models.CharField(max_length=100)
    
    task_status = models.CharField(max_length=50, choices=TASK_STATUS)
    task_description = models.TextField()
    start_date = models.DateField()
    estimate_date = models.DateField()
    file_attachment = models.FileField() 
    
