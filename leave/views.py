from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.views import View
from django.views.generic.list import ListView
from .forms import LeaveApplicationForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import EmployeeLeave, LeaveBalance
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.db.models import Sum, F
from .models import EmployeeLeave, LeaveBalance
from datetime import datetime
from users.models import Employee


# Create your views here.


def LeaveBalanceView(request):
    leave_allowed = 18  
    logged_in_user = request.user.employee

    today = datetime.today()
    month_start = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    leave_records = EmployeeLeave.objects.filter(
        employee=logged_in_user,
        status='Approved',
        start_date__month=month_start.month,
        end_date__month=month_start.month
    )
    for leave_record in leave_records:
        leave_taken = sum((leave_record.end_date - leave_record.start_date).total_seconds()) / (8 * 3600)  
        leave_remain = leave_allowed - leave_taken
         
    leave_balance = LeaveBalance.objects.get(employee=logged_in_user, month=month_start)
    if leave_balance:
        leave_balance.leave_allowed = max(0, leave_remain)  
        leave_balance.save()
    else: 
        leave_balance=LeaveBalance.objects.create(
        employee=logged_in_user,
        month=month_start,
        leave_allowed=max(0, leave_remain), 
        penalty=0
        )
        leave_balance.save()

    context = {
        'leave_allowed': leave_allowed,
        'leave_taken': leave_taken,
        'leave_remain': max(0, leave_remain), 
    }

    return render(request, 'leave/leave-balance.html', context)

class LeaveApplication(View):
    form = LeaveApplicationForm
    template_name = 'leave/leave-application.html'

    def get(self, request):

        return render(request, self.template_name, {'form' : self.form})
    
    def post(self, request):

        form = self.form(request.POST)
        if form.is_valid():
           type = form.cleaned_data['type']
           by = request.user.employee
           email = form.cleaned_data['manager']
           reason = form.cleaned_data['reason']
           start_date = form.cleaned_data['start_date']
           end_date = form.cleaned_data['end_date']
           leave_choice = form.cleaned_data['leave_choice']
           subject = 'Application for leave'
           recipient_name = form.cleaned_data['manager']
           html_template = get_template('leave/leave.html')
           html_content = html_template.render({'type': type,'recipient_name' : recipient_name,'reason': reason, 'start_date':start_date,'end_date' : end_date, 'leave_choice' :  leave_choice, 'by' : by })
           email = EmailMultiAlternatives(
               subject,
               'I am writing this to ask for leave in advance.',
               settings.EMAIL_HOST_USER,
               [email],
           )
           email.content_subtype = 'html'
           email.attach_alternative(html_content, 'text/html')
           email.send()
           form.save()

           return HttpResponse('Email sent successfully')
        
        return render(request, self.template_name, {'form' : form})
    

class MyLeave(ListView):
    model = EmployeeLeave
    template_name = 'leave/my-leave.html'

# def LeaveBalanceView(request):

#     leave_allowed = 18
#     loggedInUser = request.user.employee
#     print(loggedInUser)
#     leave_taken = EmployeeLeave.objects.filter(employee = loggedInUser, status = 'Approved')
#     print(leave_taken)
#     leave_remain = leave_allowed - leave_taken
#     leavebalance = LeaveBalance.objects.filter(employee = loggedInUser)
    
#     leavebalance.leave_taken = leave_taken
    
#     context = {
#         'leave_allowed' : leave_allowed,
#         'leave_taken' : leave_taken,
#         'leave_remain' : leave_remain,
#     }

#     return render(request, 'leave/leave-balance.html', context)


def LeaveApproveReject(request, id):

    if request.method == 'POST':
        leave_request = get_object_or_404(EmployeeLeave, id=id)
        print(leave_request)
        action = request.POST.get('action', '')
        if action == 'approve':
            leave_request.status = 'Approved'
            leave_request.save()
            return HttpResponseRedirect('/leave/manage-leave/')
        elif action == 'reject':
            leave_request.status = 'Rejected'
            leave_request.save()
            return HttpResponseRedirect('/leave/manage-leave/')

    return render(request, 'leave/manage-leave.html')


class ManageLeaveApplication(ListView):
    model = EmployeeLeave
    exclude_fields = ['manager']
    template_name = 'leave/manage-leave.html'







