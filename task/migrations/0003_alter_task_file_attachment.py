# Generated by Django 4.2.6 on 2023-10-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_rename_name_task_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='file_attachment',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
