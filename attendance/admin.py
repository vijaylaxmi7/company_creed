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
    list_display = ('employee', 'date', 'checkInTime', 'checkOutTime')

    # def formatted_total_hours_worked(self, obj):
    #     if obj.totalHoursWorked:
    #         total_hours = timezone.timedelta.total_seconds(obj.totalHoursWorked) / 3600  # Convert to hours
    #         return f"{total_hours:.2f} hours"
    #     return "N/A"
    # formatted_total_hours_worked.short_description = 'Total Hours Worked'


    

admin.site.register(Attendance, AttendanceAdmin)
# admin.site.register(Attendance, AttendanceField)

