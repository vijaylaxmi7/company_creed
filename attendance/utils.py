from datetime import timedelta
from .models import Attendance, TotalWorkingHours
import datetime
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.db.models import Sum
from users.models import Employee



def calculate_total_working_hours(id):
    
    today = datetime.now().date()
    first_day_of_month = today.replace(day=1)
    working_hours_entries = TotalWorkingHours.objects.filter(
        employee=id,
        date__gte=first_day_of_month,
        date__lte=today
    )
    total_working_hours_month = working_hours_entries.aggregate(Sum('work_hours'))['work_hours__sum'] 
    print(total_working_hours_month)

    return total_working_hours_month

def total_working_hour(request):
    logged_in_user = request.user.employee
    attendance = Attendance.objects.filter(employee=logged_in_user, date=datetime.today()).last()
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
    logged_in_user = request.user.employee
    attendance = Attendance.objects.filter(employee=logged_in_user, date=datetime.today())
    
    work_hours = timedelta(seconds=0)
    
    for obj in range(len(attendance)):
        difference = attendance[obj].time_difference
        if difference:
            work_hours += timedelta(seconds=difference.seconds)

    is_entry = TotalWorkingHours.objects.filter(employee=logged_in_user, date=datetime.today()).first()

    if is_entry:
        is_entry.work_hours = work_hours
        is_entry.save()
    else:
        total_working_hours = TotalWorkingHours(employee=logged_in_user, work_hours=work_hours)
        total_working_hours.save()

    return work_hours


    

        