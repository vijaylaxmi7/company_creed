# Generated by Django 4.2.6 on 2023-11-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0003_alter_attendance_checkout_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="time_difference",
            field=models.DurationField(null=True),
        ),
    ]
