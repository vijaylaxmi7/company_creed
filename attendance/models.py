from django.db import models
import datetime
from django.utils.duration import _get_duration_components




from users.models import Employee


class Attendance(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()

    total_working_hours = models.DurationField()
    


    


    


    



    
