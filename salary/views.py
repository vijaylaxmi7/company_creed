
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .utils import calculate_net_salary
from .models import Salary
from .forms import PaymentForm
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

class CreatePayment(View):
    template_name = 'salary/make-payment.html'

    def get(self, request, id):
        employee = Employee.objects.get(pk=id)

        if not employee.stripe_customer_id:
            customer = stripe.Customer.create(email=employee.email)
            employee.stripe_customer_id = customer.id
            employee.save()

        return render(request, self.template_name, {'employee': employee})

    def post(self, request, id):
        employee = Employee.objects.get(pk=id)
        form = PaymentForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['net_salary']
            intent = stripe.PaymentIntent.create(
                customer=employee.stripe_customer_id,
                payment_method="pm_card_visa",
                amount=amount,  
                currency='usd',
                confirm=True,
                return_url = 'http://127.0.0.1:8000/salary/success-page/'
            )

            return redirect('success_page')

        return render(request, self.template_name, {'employee': employee, 'form': form})

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





