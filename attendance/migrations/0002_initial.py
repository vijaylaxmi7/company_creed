# Generated by Django 4.2.6 on 2023-11-19 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("attendance", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailyworkinghours",
            name="employee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.employee"
            ),
        ),
        migrations.AddField(
            model_name="attendance",
            name="employee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.employee"
            ),
        ),
    ]
