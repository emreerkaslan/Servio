# Generated by Django 4.0 on 2021-12-31 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='giver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='giver', to='user.user'),
        ),
        migrations.AddField(
            model_name='service',
            name='requests',
            field=models.ManyToManyField(related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='service',
            name='taker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='taker', to='user.user'),
        ),
    ]