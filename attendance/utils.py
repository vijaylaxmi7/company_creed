from datetime import timedelta
from .models import Attendance, TotalWorkingHours
import datetime
from datetime import datetime

def total_working_hour(request):
    loggedInUser = request.user.employee
    attendance = Attendance.objects.filter(employee=loggedInUser, date=datetime.today()).last()
    time_difference = timedelta(hours=0)
    
    if attendance.checkin_time and attendance.checkout_time:
        inTime = attendance.checkin_time
        outTime = attendance.checkout_time

        inTime_delta = timedelta(hours=inTime.hour, minutes=inTime.minute, seconds=inTime.second)
        outTime_delta = timedelta(hours=outTime.hour, minutes=outTime.minute, seconds=outTime.second)

        time_difference = outTime_delta - inTime_delta

        attendance.time_difference = time_difference
        attendance.save()

    return time_difference

def total_working_hour_of_day(request):
    loggedInUser = request.user.employee
    attendance = Attendance.objects.filter(employee=loggedInUser, date=datetime.today())
    
    work_hours = timedelta(seconds=0)
    
    for obj in range(len(attendance)):
        difference = attendance[obj].time_difference
        if difference:
            work_hours += timedelta(seconds=difference.seconds)

    is_entry = TotalWorkingHours.objects.filter(employee=loggedInUser, date=datetime.today()).first()

    if is_entry:
        is_entry.work_hours = work_hours
        is_entry.save()
    else:
        total_working_hours = TotalWorkingHours(employee=loggedInUser, work_hours=work_hours)
        total_working_hours.save()

    return work_hours
    

        