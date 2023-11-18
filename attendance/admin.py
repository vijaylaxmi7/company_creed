from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Attendance, DailyWorkingHours

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id','employee', 'date', 'checkin_time', 'checkout_time', 'time_difference')

class TotalWorkingHoursAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee',  'date', 'work_hours')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(DailyWorkingHours, TotalWorkingHoursAdmin)


