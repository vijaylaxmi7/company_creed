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
from datetime import timedelta
from datetime import datetime
import locale
from .utils import TotalWorkingHour



class CreateCheckInOutTime(View):
    def get(self, request):
        if request.user.is_authenticated:
            loggedInUser = request.user.employee  
            today = datetime.today()

            isEntry = Attendance.objects.filter(employee=loggedInUser, date=today).exists()

            if isEntry:
                attendance = Attendance.objects.filter(employee=loggedInUser, date=today)
                for obj in attendance:
                    obj.checkOutTime = timezone.now()
                    obj.save()
            else:
                createCheckInTime = Attendance.objects.create(
                    employee=loggedInUser,
                    checkInTime=timezone.now(),
                    date=today
                )
                createCheckInTime.save()

            totalHoursWorked = TotalWorkingHour(request)

            return HttpResponse('success')
        
        return render(request, 'users/index.html')  
        


class CheckInOutStatus(ListView):
     
     model = Attendance
     fields = ['employee', 'checkInTime', 'checkOutTime', 'date']
     template_name = 'attendance/check-in-out.html'








# def CreateCheckInOutTime(request):
#     loggedInUser = request.user.employee
#     if loggedInUser.is_authenticated:
#         isEntry = Attendance.objects.filter(employee=loggedInUser, date=datetime.today()).exists()
#         if isEntry:
#             attendance = Attendance.objects.filter(employee=loggedInUser, date=datetime.today())
#             for obj in attendance:
#                 obj.checkOutTime = timezone.now()
#                 obj.save()
#             return HttpResponse('success')
#         else:
#             createCheckInTime = Attendance.objects.create(employee=loggedInUser, checkInTime=timezone.now(), date=datetime.today())
#             createCheckInTime.save()

#         return HttpResponse('success')

#     return render(request, 'users/index.html')







# def TotalWorkingHour(request):
#     loggedInUser = request.user.employee
#     attendance = Attendance.objects.filter(employee=loggedInUser, date=datetime.today()).last()

#     if attendance.checkInTime and attendance.checkOutTime:
#         inTime = attendance.checkInTime
#         outTime = attendance.checkOutTime
#         print(inTime)
    
#         inTime_delta = timedelta( hours= inTime.hour, minutes=inTime.minute, seconds= inTime.second)
#         outTime_delta = timedelta( hours= outTime.hour, minutes=outTime.minute, seconds= outTime.second)
#         print(outTime_delta)
#         totalHoursWorked = outTime_delta - inTime_delta
#         print(totalHoursWorked)
        
        
#         attendance.totalHoursWorked = totalHoursWorked
#         attendance.save()


#     context = {
#         'totalHoursWorked':totalHoursWorked
#     }
#     return render(request, 'attendance/check-in-out.html', context)




     






    

    


