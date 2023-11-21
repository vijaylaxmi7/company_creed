from django import forms
from .models import SalarySlipGeneration
from django.forms import ModelForm
from users.models import Employee


class PaymentForm(forms.ModelForm):

    class Meta:
        model = SalarySlipGeneration
        fields = ['employee']
        labels = {
            'net_salary' : 'amount'
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [ 'email']