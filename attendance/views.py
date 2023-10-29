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
            cache.set(f'user_{loggedInUser.id}_check_status', 'check-out', 3600)
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
     



    

    


