from .models import EmployeeLeave
from datetime import datetime

def total_leave_taken(request): 
    
    logged_in_user = request.user.employee
    today = datetime.today()
    year_start = today.replace(month=1,day=1, hour=0, minute=0, second=0, microsecond=0)
    leave_records = EmployeeLeave.objects.filter(
        employee=logged_in_user,
        status='Approved',
        start_date__year=year_start.year,
        end_date__year=year_start.year
    )
    leave_taken = 0
    for leave_record in leave_records:
        leave_taken += (leave_record.end_date - leave_record.start_date).days + 1   
    return leave_taken

def leave_type(request):

    logged_in_user = request.user.employee

    casual_leave_taken = sum(
        (leave.end_date - leave.start_date).days + 1
        for leave in EmployeeLeave.objects.filter(
            employee=logged_in_user,
            status='Approved',
            type='CASUAL LEAVE'
        )
    )

    compoff_leave_taken = sum(
        (leave.end_date - leave.start_date).days + 1
        for leave in EmployeeLeave.objects.filter(
            employee=logged_in_user,
            status='Approved',
            type='COMPOFF'
        )
    )

    optional_leave_taken = sum(
        (leave.end_date - leave.start_date).days + 1
        for leave in EmployeeLeave.objects.filter(
            employee=logged_in_user,
            status='Approved',
            type='OPTIONAL LEAVE'
        )
    )

    paid_leave_taken = sum(
        (leave.end_date - leave.start_date).days + 1
        for leave in EmployeeLeave.objects.filter(
            employee=logged_in_user,
            status='Approved',
            type='PAID_LEAVE'
        )
    )

    return casual_leave_taken, compoff_leave_taken, optional_leave_taken, paid_leave_taken
