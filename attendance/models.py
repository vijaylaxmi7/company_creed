from django.db import models
import datetime
from users.models import Employee


class Attendance(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    checkin_time = models.TimeField()
    checkout_time = models.TimeField(null=True)
    time_difference = models.DurationField(null=True)
    

class TotalWorkingHours(models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_hours = models.DurationField()    
    date = models.DateField(null=True, auto_now_add=True)





    


    



    
