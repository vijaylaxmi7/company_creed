# Generated by Django 4.2.6 on 2023-11-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("salary", "0005_alter_salaryslipgeneration_payslip_generation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salaryslipgeneration",
            name="salary_deduction",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
