# Generated by Django 4.0 on 2022-01-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_initial'),
        ('user', '0003_user_feedbacks_user_following_user_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='service',
            field=models.ManyToManyField(blank=True, null=True, related_name='services', to='service.Service'),
        ),
    ]
