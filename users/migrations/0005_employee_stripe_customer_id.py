# Generated by Django 4.2.6 on 2023-11-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_customuser_date_of_birth"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="stripe_customer_id",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
