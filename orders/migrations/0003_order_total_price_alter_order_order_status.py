# Generated by Django 4.2.5 on 2024-04-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(2, 'ORDER_PROCESSING'), (2, 'ORDER_PROCESSED'), (4, 'ORDER_DELIVERED'), (5, 'ORDER_REJECTED')], default=0),
        ),
    ]
