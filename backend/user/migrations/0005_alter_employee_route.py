# Generated by Django 5.0.3 on 2024-05-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_employee_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='route',
            field=models.TextField(blank=True, null=True),
        ),
    ]