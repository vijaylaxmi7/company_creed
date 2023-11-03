from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Attendance
from django import forms
from django.forms import widgets
from .forms import AttendanceForm



# Register your models here.



# class AttendanceField(admin.ModelAdmin):
#     list_display = ['id', 'totalHoursWorked', 'checkInTime', 'checkOutTime']
#     form = AttendanceForm

    


admin.site.register(Attendance)
# admin.site.register(Attendance, AttendanceField)

