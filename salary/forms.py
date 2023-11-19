from django import forms
from .models import SalarySlipGeneration
from django.forms import ModelForm


class PaymentForm(forms.ModelForm):

    class Meta:
        model = SalarySlipGeneration
        fields = ['employee', 'net_salary']
        labels = {
            'net_salary' : 'amount'
        }

    