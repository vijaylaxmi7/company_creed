from .models import Attendance
import datetime
from datetime import timedelta
from django.utils import timezone

def calculate_total_hours_worked(employee, date=None):
    if date is None:
        date = timezone.localdate()

    attendances = Attendance.objects.filter(employee=employee, date=date)
    total_duration = timedelta()

    for attendance in attendances:
        if attendance.checkInTime and attendance.checkOutTime:
            worked_duration = attendance.checkOutTime - attendance.checkInTime
            total_duration += worked_duration

    total_seconds = total_duration.total_seconds()
    total_hours = total_seconds / 3600  

    return total_hours