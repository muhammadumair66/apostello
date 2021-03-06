# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-04 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='disable_email_login_form',
            field=models.BooleanField(default=False, help_text='Tick this to hide the login with email form. Note, you will need to have setup login with Google, or users will have no way into the site.'),
        ),
    ]
