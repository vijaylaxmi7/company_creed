from datetime import timedelta
from django.utils import timezone
from .models import Attendance  
import datetime
from datetime import datetime

def TotalWorkingHour(request):
    loggedInUser = request.user.employee
    attendance = Attendance.objects.filter(employee=loggedInUser, date=datetime.today()).last()
    total_working_hours = timedelta(hours=0)
    
    if attendance.checkin_time and attendance.checkout_time:
        inTime = attendance.checkin_time
        outTime = attendance.checkout_time

        inTime_delta = timedelta(hours=inTime.hour, minutes=inTime.minute, seconds=inTime.second)
        outTime_delta = timedelta(hours=outTime.hour, minutes=outTime.minute, seconds=outTime.second)

        total_working_hours = outTime_delta - inTime_delta

        attendance.total_working_hours = total_working_hours
        attendance.save()

    return total_working_hours