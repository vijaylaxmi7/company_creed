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
    task = models.CharField(max_length=50)
    project = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=TASK_STATUS)
    description = models.TextField()
    start_date = models.DateField()
    estimate_date = models.DateField()
    file_attachment = models.FileField(upload_to='documents/') 

    def __str__(self):

        return self.task
    

    
