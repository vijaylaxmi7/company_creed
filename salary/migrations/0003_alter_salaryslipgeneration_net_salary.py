# Generated by Django 4.2.6 on 2023-11-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("salary", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salaryslipgeneration",
            name="net_salary",
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]
