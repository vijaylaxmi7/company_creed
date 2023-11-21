from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.views import View
from django.views.generic.list import ListView
from .forms import LeaveApplicationForm
from django.http import HttpResponseRedirect
from .models import EmployeeLeave
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from datetime import datetime
from .utils import total_leave_taken, leave_type

# Create your views here.



class LeaveApplication(View):
    form = LeaveApplicationForm
    template_name = 'leave/leave-application.html'

    def get(self, request):

        return render(request, self.template_name, {'form' : self.form})
    
    def post(self, request):

        form = self.form(request.POST, request = request)
        
        if form.is_valid():
        
           form.instance.employee = request.user.employee 
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
           
           return HttpResponseRedirect('/leave/my-leave/')
        
        return render(request, self.template_name, {'form' : form})
    
class MyLeave(ListView):
    model = EmployeeLeave
    template_name = 'leave/my-leave.html'


def LeaveBalanceView(request):
    logged_in_user = request.user.employee
    today = datetime.today()
    year_start = today.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    leave_taken = total_leave_taken(request)
    leave_remain = logged_in_user.annual_leave - leave_taken

    leave_balance = EmployeeLeave.objects.filter(
        employee=logged_in_user,
        start_date__month=year_start.month  
    ).first()

    if leave_balance:
        leave_balance.leave_allowed = leave_remain
        leave_balance.save()
    else:
        EmployeeLeave.objects.create(
            employee=logged_in_user,
            start_date=year_start,
        )
    return render(request, 'leave/leave-balance.html', {
        'annual_leave': logged_in_user.annual_leave,
        'leave_taken': leave_taken,
        'leave_remain': leave_remain,
        'casual_leave': leave_type(request)[0],
        'compoff_leave': leave_type(request)[1],
        'optional_leave': leave_type(request)[2],
        'paid_leave': leave_type(request)[3],
        'leave_month': leave_balance.start_date.strftime("%B"),  
        
    })

class LeaveApproveRejectView(View):

    template_name = 'leave/manage-leave.html'

    def post(self, request, id):

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







