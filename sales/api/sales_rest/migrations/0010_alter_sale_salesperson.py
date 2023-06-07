# Generated by Django 4.0.3 on 2023-06-07 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0009_alter_salesperson_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='salesperson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salesperson', to='sales_rest.salesperson'),
        ),
    ]
