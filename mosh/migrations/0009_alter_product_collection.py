# Generated by Django 4.0.6 on 2022-10-18 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mosh', '0008_alter_employee_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='mosh.collection'),
        ),
    ]
