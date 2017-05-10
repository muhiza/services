# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-10 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_auto_20170510_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='about_us',
            field=models.TextField(help_text=b'Enter the story about you', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='mission',
            field=models.TextField(help_text=b'Enter your mission', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='values',
            field=models.TextField(help_text=b'Enter your mission', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='vision',
            field=models.TextField(help_text=b'Enter your vision', max_length=300, null=True),
        ),
    ]
