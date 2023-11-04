from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Attendance
from django import forms
from django.forms import widgets
from .forms import AttendanceForm
from django.utils import timezone



# Register your models here.



class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'checkInTime', 'checkOutTime', 'totalHoursWorked')


admin.site.register(Attendance, AttendanceAdmin)


