# Generated by Django 4.0.3 on 2023-06-06 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0008_alter_automobilevo_import_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesperson',
            name='employee_id',
            field=models.CharField(max_length=20),
        ),
    ]
