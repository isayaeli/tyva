# Generated by Django 3.2.4 on 2021-06-19 14:17

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default=django.contrib.auth.models.User),
        ),
    ]
