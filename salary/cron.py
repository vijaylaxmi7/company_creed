from django_cron import CronJobBase, Schedule
from .views import GenerateSalarySlip
from .models import Employee


class GenerateSalarySlipCronJob(CronJobBase):
    # RUN_EVERY_MN = 60 * 24 * 30  
    RUN_EVERY_MN = 1


    schedule = Schedule(run_every_mins=RUN_EVERY_MN)
    code = 'salary.generate_salary_slip_cron_job'  

    def do(self):
        print('send')
        for employee in Employee.objects.all():
            GenerateSalarySlip().get(None, id=employee.id)


