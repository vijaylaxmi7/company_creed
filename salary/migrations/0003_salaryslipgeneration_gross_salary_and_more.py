# Generated by Django 4.2.6 on 2023-11-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("salary", "0002_remove_salaryslipgeneration_gross_salary_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="salaryslipgeneration",
            name="gross_salary",
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name="salaryslipgeneration",
            name="net_salary",
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name="salaryslipgeneration",
            name="salary_deduction",
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]