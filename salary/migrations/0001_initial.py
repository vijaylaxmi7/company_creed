# Generated by Django 4.2.6 on 2023-11-18 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0002_employee_annual_leave"),
    ]

    operations = [
        migrations.CreateModel(
            name="SalarySlipGeneration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gross_salary", models.DecimalField(decimal_places=2, max_digits=20)),
                ("net_salary", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "salary_deduction",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("payslip_generation_date", models.DateTimeField()),
                ("remarks", models.TextField(blank=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.employee"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Salary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("basic_salary", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "provident_fund",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("allowance", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "tax_rate",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
                ),
                ("salary_period", models.CharField(max_length=20)),
                (
                    "employee",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="users.employee"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BankAccountDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bank_name", models.CharField(max_length=60)),
                ("account_no", models.CharField(max_length=30)),
                ("ifsc_code", models.CharField(max_length=11)),
                ("branch", models.CharField(max_length=30)),
                ("is_active", models.BooleanField(default=False)),
                ("employee_status", models.CharField(default="Active", max_length=10)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.employee"
                    ),
                ),
            ],
        ),
    ]
