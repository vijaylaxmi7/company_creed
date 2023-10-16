from django.contrib import admin
from .models import Employee, Designation, Technology

# Register your models here.


# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Employee)
admin.site.register(Designation)
admin.site.register(Technology)
