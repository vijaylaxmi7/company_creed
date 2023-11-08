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
            print('yes')
            loggedInUser = request.user.employee  
            print(loggedInUser)
            isEntry = Attendance.objects.filter(employee=loggedInUser, date=datetime.today()).order_by('date')
            print(isEntry)
            if isEntry.exists():
                print('inter')
                isEntry = isEntry[len(isEntry)-1]
                print(isEntry)
                if isEntry.checkin_time and isEntry.checkout_time:
                    print("checkin")
                    createCheckInTime = Attendance.objects.create(
                        employee=loggedInUser,
                        checkin_time=timezone.now(),
                        date=datetime.today()
                    )
                    createCheckInTime.save()
                elif isEntry.checkin_time:
                    print("checkout")
                    isEntry.checkout_time = timezone.now()
                    isEntry.save()

            else: 
                print('checkin')
                createCheckInTime = Attendance.objects.create(
                        employee=loggedInUser,
                        checkin_time=timezone.now(),
                        date=datetime.today()
                    )
                createCheckInTime.save()


            
                    
            # attendance = Attendance.objects.get(employee = loggedInUser, date = datetime.today())
            # for attendance in isEntry:
            #      if attendance.checkInTime and attendance.checkOutTime:
            #         createCheckInTime = Attendance.objects.create(
            #         employee=loggedInUser,
            #         checkInTime=timezone.now(),
            #         date=datetime.today()
            #     )
            #         createCheckInTime.save()
            #         break


            # total_working_hours = TotalWorkingHour(request)

            return HttpResponse('success')
        
        return render(request, 'users/index.html')  
    

class CheckInOutStatus(ListView):
     
     model = Attendance
     fields = ['employee', 'checkin_time', 'checkout_time', 'date']
     template_name = 'attendance/check-in-out.html'
     paginate_by = 1

     def get_queryset(self):
        return Attendance.objects.all().order_by('-checkin_time').values()

        


# class CreateCheckInOutTime(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             loggedInUser = request.user.employee  
#             isEntry = Attendance.objects.filter(employee=loggedInUser, date=datetime.today())

#             if isEntry.exists():
#                 attendance = Attendance.objects.filter(employee=loggedInUser, date=datetime.today())
#                 for obj in attendance:
#                     obj.checkOutTime = timezone.now()
#                     obj.save()
#             else:
#                     createCheckInTime = Attendance.objects.create(
#                         employee=loggedInUser,
#                         checkInTime=timezone.now(),
#                         date=datetime.today()
#                     )
#                     createCheckInTime.save()
                    
#             # attendance = Attendance.objects.get(employee = loggedInUser, date = datetime.today())
#             for attendance in isEntry:
#                  if attendance.checkInTime and attendance.checkOutTime:
#                     createCheckInTime = Attendance.objects.create(
#                     employee=loggedInUser,
#                     checkInTime=timezone.now(),
#                     date=datetime.today()
#                 )
#                     createCheckInTime.save()
#                     break


#             totalHoursWorked = TotalWorkingHour(request)

#             return HttpResponse('success')
        
#         return render(request, 'users/index.html')  
        












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




     






    

    


