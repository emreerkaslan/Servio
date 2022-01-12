# Generated by Django 4.0 on 2022-01-02 13:44

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='feedbackGiven',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='picture',
            field=models.CharField(default='https://bcw.org.au/wp-content/uploads/2020/02/BCWS-rebrand-37-2048x668.png', max_length=511, verbose_name='picture'),
        ),
        migrations.AddField(
            model_name='service',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255, verbose_name='tag'), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='service',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='service',
            name='requests',
            field=models.ManyToManyField(blank=True, null=True, related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
