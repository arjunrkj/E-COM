# Generated by Django 4.2.5 on 2024-03-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
