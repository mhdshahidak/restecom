# Generated by Django 4.0.6 on 2022-10-11 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoping', '0002_alter_cartitems_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='price',
            field=models.IntegerField(),
        ),
    ]