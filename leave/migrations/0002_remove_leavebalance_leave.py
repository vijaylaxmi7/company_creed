# Generated by Django 4.2.6 on 2023-11-14 21:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("leave", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="leavebalance",
            name="leave",
        ),
    ]
