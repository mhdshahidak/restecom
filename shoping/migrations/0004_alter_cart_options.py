# Generated by Django 4.0.6 on 2022-10-17 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoping', '0003_alter_cartitems_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'permissions': [('cancel_order', 'Can cancel Order')]},
        ),
    ]
