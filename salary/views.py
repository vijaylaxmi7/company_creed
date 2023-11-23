
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .utils import calculate_net_salary
from .models import Salary
from .forms import AccountCreationForm
from django.http import JsonResponse
from users.models import Employee
from .models import SalarySlipGeneration
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from .utils import calculate_gross_salary, calculate_net_salary, calculate_salary_deduction, send_salary_slip
import stripe
from django.conf import settings

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCustomer(View):
    template_name = "salary/create-account.html"
    form_class = AccountCreationForm  

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['employee']
            try:
                customer = stripe.Customer.create(
                email=email,
                payment_method="pm_card_visa",
                invoice_settings={"default_payment_method": "pm_card_visa"},
                )
                employee = Employee.objects.get(id = email.id)
                employee.stripe_customer_id = customer.id
                employee.save()
                return JsonResponse({'status': 'success', 'message': 'Customer created successfully'})
            except stripe.error.StripeError as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        return render(request, self.template_name, {'form': form})
    

class CreateCheckoutSession(View):
    template_name = "salary/create-checkout-session.html"
    form_class = AccountCreationForm  

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['employee']
            try:
                session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    mode='setup',
                    customer=email.stripe_customer_id, 
                    success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url='https://example.com/cancel',
                )
                return JsonResponse({'status': 'success', 'message': 'Checkout session created successfully', 'session_id': session.id, 'payout' : payout.id})
            except stripe.error.StripeError as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        return render(request, self.template_name, {'form': form})

def success_page(request):
    return render(request, 'salary/success.html')

class GenerateSalarySlip(View):

    template_name = 'salary/generate-salary-slip.html'

    def get(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        salary_instance = Salary.objects.get(employee=employee)

        context = {
            'employee': employee,
            'basic_salary': salary_instance.basic_salary,
            'provident_fund': salary_instance.provident_fund,
            'allowance': salary_instance.allowance,
            'gross_salary': calculate_gross_salary(id),
            'salary_deduction': calculate_salary_deduction(id),
            'net_salary':calculate_net_salary(id) ,
            'payslip_generation_date': datetime.now(),  
            
        }
        send_salary_slip(id)

        return render(request, self.template_name, context)
    
class DownloadSalarySlipView(View):
    def get(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        salary_instance = Salary.objects.get(employee=employee)

        context = {
            'employee': employee,
            'basic_salary': salary_instance.basic_salary,
            'provident_fund': salary_instance.provident_fund,
            'allowance': salary_instance.allowance,
            'gross_salary': calculate_gross_salary(id),
            'salary_deduction': calculate_salary_deduction(id),
            'net_salary': calculate_net_salary(id),
            'payslip_generation_date': datetime.now(),
        }

        template = get_template('salary/salary-slip-template.html')
        html_content = template.render(context)

        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename=salary_slip_{employee.id}.html'
        response.write(html_content)
        return response
    
class EmployeeListView(ListView):
    model = Employee
    template_name = "salary/employee-list.html"

class UserSalarySlipView(ListView):
    template_name = 'salary/list-salary-slip.html'
    model = SalarySlipGeneration
    context_object_name = 'salary'

    def get_queryset(self):
        employee = self.request.user.employee
        salary_data = SalarySlipGeneration.objects.filter(
            employee=employee,
        )
        return salary_data





