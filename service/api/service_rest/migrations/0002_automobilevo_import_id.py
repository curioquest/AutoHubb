# Generated by Django 4.0.3 on 2023-06-06 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobilevo',
            name='import_id',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]