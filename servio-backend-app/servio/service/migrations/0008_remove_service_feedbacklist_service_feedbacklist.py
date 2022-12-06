# Generated by Django 4.0 on 2022-01-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_alter_feedback_taker'),
        ('service', '0007_remove_service_feedbackgiven_service_feedbacklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='feedbackList',
        ),
        migrations.AddField(
            model_name='service',
            name='feedbackList',
            field=models.ManyToManyField(blank=True, null=True, related_name='feedbackList', to='feedback.Feedback'),
        ),
    ]