# Generated by Django 3.2.4 on 2021-07-06 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_date',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_date',
            new_name='start_time',
        ),
    ]
