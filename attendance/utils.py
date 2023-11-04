from datetime import timedelta
from django.utils import timezone
from .models import Attendance  
import datetime
from datetime import datetime

def TotalWorkingHour(request):
    loggedInUser = request.user.employee
    attendance = Attendance.objects.filter(employee=loggedInUser, date=datetime.today()).last()
    totalHoursWorked = timedelta(hours=0)
    
    if attendance.checkInTime and attendance.checkOutTime:
        inTime = attendance.checkInTime
        outTime = attendance.checkOutTime

        inTime_delta = timedelta(hours=inTime.hour, minutes=inTime.minute, seconds=inTime.second)
        outTime_delta = timedelta(hours=outTime.hour, minutes=outTime.minute, seconds=outTime.second)

        totalHoursWorked = outTime_delta - inTime_delta

        attendance.totalHoursWorked = totalHoursWorked
        attendance.save()

    return totalHoursWorked