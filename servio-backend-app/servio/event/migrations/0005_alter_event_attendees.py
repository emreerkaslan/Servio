# Generated by Django 4.0 on 2022-01-02 13:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0004_event_picture_alter_event_attendees_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='attendee', to=settings.AUTH_USER_MODEL),
        ),
    ]
