# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-08 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_auto_20170506_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(default=1, upload_to=b''),
        ),
    ]