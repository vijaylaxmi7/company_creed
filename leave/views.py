from django.shortcuts import render

from django.shortcuts import render

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .forms import leaveApplicationForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, request
from .models import EmployeeLeave
from users.models import Employee, CustomUser
from users.views import index
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from django.core.mail import EmailMessage, get_connection, send_mail
from django.template import Context, Template, RequestContext

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import uuid

from users.helpers import send_leave_email

from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings



# Create your views here.


class ManageLeaveApplication(ListView):
    model = EmployeeLeave
    exclude_fields = ['manager']
    template_name = 'leave/manage-leave.html'




def SendStatus(request):

    if request.method == 'POST':
        status = request.POST.get("status")
        email = request.POST.get("employee")
        recipient_name = request.POST.get("employee")
        subject = 'Application for leave'
        html_template = get_template('leave/leave.html')
        html_content = html_template.render({'type': type,'recipient_name' : recipient_name,'status': status })
        email = EmailMultiAlternatives(
               subject,
               'I am writing this to ask for leave in advance.',
               settings.EMAIL_HOST_USER,
               [email],
           )
        email.attach_alternative(html_content, 'leave/leave.html')
        email.send()
        return HttpResponse('Email sent successfully')
    return render(request, "leave/manage-leave.html")
    

class LeaveApplication(View):
    form = leaveApplicationForm
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
           startDate = form.cleaned_data['startDate']
           endDate = form.cleaned_data['endDate']
           leaveChoice = form.cleaned_data['leaveChoice']
           subject = 'Application for leave'
           recipient_name = form.cleaned_data['manager']
           html_template = get_template('leave/leave.html')
           html_content = html_template.render({'type': type,'recipient_name' : recipient_name,'reason': reason, 'startDate':startDate,'endDate' : endDate, 'leaveChoice' :  leaveChoice, 'by' : by })
           email = EmailMultiAlternatives(
               subject,
               'I am writing this to ask for leave in advance.',
               settings.EMAIL_HOST_USER,
               [email],
           )
           email.content_subtype = 'html'
           email.attach_alternative(html_content, 'text/html')
           email.send()

           return HttpResponse('Email sent successfully')
        
        return render(request, self.template_name, {'form' : form})
    

class updateStatus(UpdateView):
    model = EmployeeLeave
    fields = ['leaveChoice']
    template_name = 'leave/manage-leave.html'
    success_url = HttpResponse('updated')




