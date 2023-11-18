from django.contrib import admin

from django.contrib import admin
from .models import EmployeeLeave

# Register your models here.
class  EmployeeLeaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee',  'start_date', 'end_date', 'status')

admin.site.register(EmployeeLeave, EmployeeLeaveAdmin)

