# Generated by Django 4.2.6 on 2023-11-18 14:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("leave", "0006_employeeleave_month"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employeeleave",
            name="month",
        ),
    ]
