# Generated by Django 4.0 on 2022-01-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_remove_service_taker_service_taker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
