from datetime import timedelta
from .models import Attendance, DailyWorkingHours
import datetime
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.db.models import Sum
from users.models import Employee
from django import template
register = template.Library()

def calculate_total_working_hours(id):
    
    today = datetime.now().date()
    first_day_of_month = today.replace(day=1)
    working_hours_entries = DailyWorkingHours.objects.filter(
        employee=id,
        date__gte=first_day_of_month,
        date__lte=today
    )
    total_working_hours_month = working_hours_entries.aggregate(Sum('work_hours'))['work_hours__sum'] 

    return total_working_hours_month

def total_time_difference(request):
    logged_in_user = request.user.employee
    attendance = Attendance.objects.filter(employee=logged_in_user, date=datetime.today()).last()
    time_difference = timedelta(hours=0)
    
    if attendance.checkin_time and attendance.checkout_time:
        in_time = attendance.checkin_time
        out_time = attendance.checkout_time

        in_time_delta = timedelta(hours=in_time.hour, minutes=in_time.minute)
        out_time_delta = timedelta(hours=out_time.hour, minutes=out_time.minute)

        time_difference = out_time_delta - in_time_delta

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

    is_entry = DailyWorkingHours.objects.filter(employee=logged_in_user, date=datetime.today()).first()

    if is_entry:
        is_entry.work_hours = work_hours
        is_entry.save()
    else:
        total_working_hours = DailyWorkingHours(employee=logged_in_user, work_hours=work_hours)
        total_working_hours.save()

    return work_hours

@register.filter()
def smooth_timedelta(timedeltaobj):

    secs = timedeltaobj.total_seconds()
    timetot = ""
    if secs > 86400: # 60sec * 60min * 24hrs
        days = secs // 86400
        timetot += "{} days".format(int(days))
        secs = secs - days*86400

    if secs > 3600:
        hrs = secs // 3600
        timetot += " {} hours".format(int(hrs))
        secs = secs - hrs*3600

    if secs > 60:
        mins = secs // 60
        timetot += " {} minutes".format(int(mins))
        secs = secs - mins*60

    if secs > 0:
        timetot += " {} seconds".format(int(secs))
    return timetot


    

        