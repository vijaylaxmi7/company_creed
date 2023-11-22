from django.shortcuts import render
from django.utils import timezone
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Attendance, DailyWorkingHours
from django.db.models import Q
from .utils import total_time_difference, total_working_hour_of_day

import datetime
from datetime import datetime

class CreateCheckInOutTimeView(View):

    def post(self, request):
        
        if request.user.is_authenticated:
            logged_in_user = request.user.employee  
            is_entry = Attendance.objects.filter(employee=logged_in_user, date=datetime.today())
            if is_entry.exists():
                is_entry = is_entry.last()
                if is_entry.checkin_time and is_entry.checkout_time:
                    createCheckInTime = Attendance.objects.create(
                        employee=logged_in_user,
                        checkin_time=timezone.now(),
                        date=datetime.today()
                    )
                    createCheckInTime.save()
                elif is_entry.checkin_time:
                    is_entry.checkout_time = timezone.now()
                    is_entry.save()
            else: 
                createCheckInTime = Attendance.objects.create(
                        employee=logged_in_user,
                        checkin_time=timezone.now(),
                        date=datetime.today()
                    )
                createCheckInTime.save()
            total_time_difference(request)
            total_working_hour_of_day(request)
            return HttpResponse('success')
        
        return render(request, 'users/index.html')  
    
class EmployeeCheckInOutView(ListView):
    model = Attendance
    fields = ['employee', 'checkin_time', 'checkout_time', 'date']
    template_name = 'attendance/check-in-out.html'
    paginate_by = 10
    ordering = ['-date']

    def get_queryset(self):
        search_query = self.request.GET.get('search_query', '')
        attendance_data = Attendance.objects.filter(Q(date__contains=search_query) 
                                                    |Q(employee__first_name__icontains = search_query)).order_by('-date')
        return attendance_data
        
class EmployeeWorkingHourView(ListView):
     
     model = DailyWorkingHours
     fields = ['employee','date', 'work_hours']
     template_name = 'attendance/total-working-hours.html'
     paginate_by = 5

     def get_queryset(self):
        search_query = self.request.GET.get('search_query', '')
        working_hour_data = DailyWorkingHours.objects.filter(Q(date__contains=search_query) 
                                                            |Q(employee__first_name__icontains = search_query)).order_by('-date')
        return working_hour_data
     
class UserCheckInOutView(ListView):
    template_name = 'attendance/user-check-in-out.html'
    context_object_name = 'attendance'
    paginate_by = 10  

    def get_queryset(self):
        search_query = self.request.GET.get('search_query', '')
        attendance_data = Attendance.objects.filter(employee=self.request.user.employee, date__contains=search_query).order_by('-date')

        for obj in attendance_data:
            if obj.time_difference is not None:
                hours, remainder = divmod(obj.time_difference.seconds, 3600)
                minutes = remainder//60
                obj.time_difference = f"{hours} hr {minutes} min"
            else:
                obj.time_difference = "Not available"

        return attendance_data
    
class UserWorkHourView(ListView):
    template_name = 'attendance/user-work-hour.html'
    context_object_name = 'work_hour'
    paginate_by = 10  

    def get_queryset(self):
        search_query = self.request.GET.get('search_query', '')
        working_hour_data = DailyWorkingHours.objects.filter(employee=self.request.user.employee, date__contains=search_query).order_by('-date')
        for obj in working_hour_data:
            hours, remainder = divmod(obj.work_hours.seconds, 3600)
            minutes = remainder//60
            obj.work_hours = f"{hours} hr {minutes} min"
        return working_hour_data
    
         







     






    

    


