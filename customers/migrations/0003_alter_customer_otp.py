# Generated by Django 4.2.5 on 2024-03-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='otp',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
