# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-18 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamlogic', '0009_auto_20170618_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, default=b'./404/profile.jpg', null=True, upload_to=b'media'),
        ),
    ]
