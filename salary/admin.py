from django.contrib import admin
from .models import Salary, SalarySlipGeneration


class SalarySlipGenerationAdmin(admin.ModelAdmin):
    list_display = ('id','employee' )


admin.site.register(Salary, SalarySlipGenerationAdmin)
admin.site.register(SalarySlipGeneration)
