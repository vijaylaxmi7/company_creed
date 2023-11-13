# Generated by Django 4.2.6 on 2023-11-10 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employee'),
        ),
        migrations.AddField(
            model_name='task',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='users.employee'),
        ),
    ]
