from .models import EmployeeLeave

def leave_balance(request):

    leave_taken = EmployeeLeave.objects.filter(employee = request.user.employee, status = 'Approved').count()
    leave_balance = EmployeeLeave.leave_allowed - leave_taken
    return leave_balance