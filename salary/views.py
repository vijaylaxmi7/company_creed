
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from .utils import calculate_net_salary
from django.shortcuts import render
from .models import Salary
from users.models import Employee
from .models import SalarySlipGeneration
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from .forms import PaymentForm
from .utils import calculate_gross_salary, calculate_net_salary, calculate_salary_deduction, send_salary_slip
import stripe
from django.conf import settings

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            amount = form.cleaned_data['amount']

            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  
                currency='usd',
            )
            SalarySlipGeneration.objects.create(employee=employee, amount=amount)
            
            client_secret = payment_intent.client_secret
            return render(request, 'salary/success.html', {'client_secret': client_secret})
    else:
        form = PaymentForm()

    return render(request, 'salary/make-payment.html', {'form': form})

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
    paginate_by = 10  

    def get_queryset(self):
        search_query = self.request.GET.get('search_query', '')
        employee = self.request.user.employee
        working_hour_data = SalarySlipGeneration.objects.filter(
            employee=employee,
        )
        return working_hour_data





