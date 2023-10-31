from django.shortcuts import render
import datetime
from django.utils import timezone
from django.shortcuts import render

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, request
from .models import Attendance
from users.models import Employee, CustomUser
from users.views import index
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.core.cache import cache
from django.db.models import DurationField, ExpressionWrapper, F, IntegerField, Value, TimeField
from django.db.models.functions import Coalesce



def TotalWorkingHour(request):

    loggedInUser = request.user.employee
    attendance = Attendance.objects.filter(employee = loggedInUser, date = datetime.date.today()).last()
    # attendance.totalHoursWorked = attendance.checkOutTime - attendance.checkInTime
    total_hours = attendance.checkOutTime - attendance.checkInTime
    attendance.totalHoursWorked  = total_hours
    attendance.save()
    
    
    context = {
        'totalHoursWorked' : total_hours
    }

    return render(request, 'attendance/check-in-out.html', context)



# def CreateCheckInTime(request):
    
#     loggedInUser = request.user.employee
#     if loggedInUser.is_authenticated:
#         createCheckInTime = Attendance.objects.create(employee = loggedInUser, checkInTime = timezone.now(), date = datetime.date.today())
#         createCheckInTime.save()
#         return HttpResponse('success')
        
#     return render(request, 'users/index.html')

# def CreateCheckOutTime(request):
       
#     loggedInUser = request.user.employee
#     if loggedInUser.is_authenticated:
#         createCheckOutTime = Attendance.objects.create(employee = loggedInUser, checkOutTime = timezone.now(), date = datetime.date.today())
#         createCheckOutTime.save()
#         return HttpResponse('success')
        
#     return render(request, 'users/index.html')
       



def CreateCheckInTime(request):
    loggedInUser = request.user.employee
    if loggedInUser.is_authenticated:
        isEntry = Attendance.objects.filter(employee=loggedInUser, date=datetime.date.today()).exists()
        print(isEntry)
        if isEntry:
            attendance = Attendance.objects.filter(employee=loggedInUser, date=datetime.date.today())
            # entry.checkOutTime = timezone.now()
            # entry.save()
            for obj in attendance:
                obj.checkOutTime = timezone.now()
                obj.save()
            return HttpResponse('success')
        else:
            createCheckInTime = Attendance.objects.create(employee=loggedInUser, checkInTime=timezone.now(), date=datetime.date.today())
            createCheckInTime.save()

            return HttpResponse('success')
    return render(request, 'users/index.html')




# def CreateCheckInTime(request):
    
#     if request.method == 'POST':
#         loggedInUser = request.user.employee
        
#         if loggedInUser.is_authenticated:
#                     if Attendance.checkOutTime:
#                         createCheckInTime = Attendance.objects.create(employee = loggedInUser, checkInTime = timezone.now(), date = datetime.date.today())
#                         createCheckInTime.save()
#                         return HttpResponse('success')
#         else:
#             createCheckOutTime = Attendance.objects.create(employee = loggedInUser, checkOutTime = timezone.now(), date = datetime.date.today())
#             createCheckOutTime.save()
#             return HttpResponse('success')
          
#     return render(request, 'users/index.html')



class CheckInOutStatus(ListView):
     
     model = Attendance
     fields = ['employee', 'checkInTime', 'checkOutTime', 'date']
     template_name = 'attendance/check-in-out.html'
     


#attendance = attendance.annotate(total_working_hours = F('checkOutTime')-F('checkInTime'))
    #print('---------->',attendance,attendance[0])
    #breakpoint()
    # attendance.update(checkOutTime=F('checkOutTime')-F('checkInTime'))
    # print('------>',attendance)
    # inTime = attendance.checkInTime
    # outTime = attendance.checkOutTime
    # totalHoursWorked = attendance.aggregate(
    # total_time=sum(ExpressionWrapper(
    #     F('checkOutTime') - F('checkInTime'), output_field=DurationField())
    # ))['total_time']



    

    


