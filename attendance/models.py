from django.db import models

from users.models import Employee

class EmployeeAttendance(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    total_working_days = models.IntegerField()
    total_present_day = models.IntegerField()
    
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    break_start = models.DateTimeField()
    break_end = models.DateTimeField()
