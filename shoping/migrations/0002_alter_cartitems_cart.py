# Generated by Django 4.0.6 on 2022-10-11 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shoping.cart'),
        ),
    ]
