from django.shortcuts import render
from django.utils import timezone
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Attendance, TotalWorkingHours
from .utils import total_working_hour, total_working_hour_of_day
import datetime

class CreateCheckInOutTimeView(View):

    def get(self, request):
        
        if request.user.is_authenticated:
            loggedInUser = request.user.employee  
            is_entry = Attendance.objects.filter(employee=loggedInUser, date=datetime.today()).order_by('date')
            if is_entry.exists():
                is_entry = is_entry[len(is_entry)-1]
                if is_entry.checkin_time and is_entry.checkout_time:
                    createCheckInTime = Attendance.objects.create(
                        employee=loggedInUser,
                        checkin_time=timezone.now(),
                        date=datetime.today()
                    )
                    createCheckInTime.save()
                elif is_entry.checkin_time:
                    is_entry.checkout_time = timezone.now()
                    is_entry.save()
            else: 
                createCheckInTime = Attendance.objects.create(
                        employee=loggedInUser,
                        checkin_time=timezone.now(),
                        date=datetime.today()
                    )
                createCheckInTime.save()
            total_working_hour(request)
            total_working_hour_of_day(request)
            return HttpResponse('success')
        
        return render(request, 'users/index.html')  
    
class EmployeeCheckInOutView(ListView):
    model = Attendance
    fields = ['employee', 'checkin_time', 'checkout_time', 'date']
    template_name = 'attendance/check-in-out.html'
    paginate_by = 5
    ordering = ['-date']

    def get_queryset(self):
        search_query = self.request.GET.get('search_query', '')
        attendance_data = Attendance.objects.filter(date__contains=search_query)
        return attendance_data
        
class EmployeeWorkingHourView(ListView):
     
     model = TotalWorkingHours
     fields = ['employee','date', 'work_hours']
     template_name = 'attendance/total-working-hours.html'
     paginate_by = 5
     ordering = ['-date']

     def get_queryset(self):
        search_query = self.request.GET.get('search_query', '')
        working_hour_data = TotalWorkingHours.objects.filter(date__contains=search_query)
        return working_hour_data
     
class UserCheckInOutView(ListView):
    template_name = 'attendance/user-check-in-out.html'
    context_object_name = 'attendance'
    paginate_by = 10  

    def get_queryset(self):
        return Attendance.objects.filter(employee=self.request.user.employee)
    

class UserWorkHourView(ListView):
    template_name = 'attendance/user-work-hour.html'
    context_object_name = 'work_hour'
    paginate_by = 10  

    def get_queryset(self):
        return TotalWorkingHours.objects.filter(employee = self.request.user.employee)
    







     






    

    


