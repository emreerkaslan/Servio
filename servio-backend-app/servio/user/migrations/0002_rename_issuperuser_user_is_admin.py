# Generated by Django 4.0 on 2021-12-31 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='isSuperuser',
            new_name='is_admin',
        ),
    ]