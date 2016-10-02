# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-02 19:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('code_checker', '0002_auto_20161002_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='codecompile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
