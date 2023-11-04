from django.db import models
import datetime
from django.utils.duration import _get_duration_components




from users.models import Employee


class Attendance(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    checkInTime = models.TimeField()
    checkOutTime = models.TimeField( null=True)
    startBreakTime = models.TimeField(null=True)
    endBreakTime = models.TimeField(null=True)
    totalHoursWorked = models.DurationField(null=True)
    


    


    


    



    
