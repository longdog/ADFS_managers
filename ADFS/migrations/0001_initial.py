# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-02 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xb8 \xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f:')),
                ('vkLink', models.CharField(max_length=40, null=True, verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xbd\xd0\xb0 \xd0\xb2\xd0\xb0\xd1\x88 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x84\xd0\xb8\xd0\xbb\xd1\x8c \xd0\xb2 \xd0\xb2\xd0\xba:')),
                ('phone', models.CharField(max_length=12, null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd \xd0\xb4\xd0\xbb\xd1\x8f \xd1\x81\xd0\xb2\xd1\x8f\xd0\xb7\xd0\xb8:')),
                ('avatar', models.ImageField(null=True, upload_to=b'', verbose_name=b'\xd0\xad\xd0\xbc\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbc\xd0\xb0 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd1\x8b:')),
                ('team', models.CharField(max_length=10, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd1\x8b:')),
                ('grundung', models.DateField(help_text=b'\xd0\x95\xd1\x81\xd0\xbb\xd0\xb8 \xd0\xb2\xd0\xb0\xd1\x88\xd0\xb0 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0 \xd0\xb1\xd1\x8b\xd0\xbb\xd0\xb0 \xd0\xbe\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb0 \xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xb5, \xd1\x83\xd0\xba\xd0\xb0\xd0\xb6\xd0\xb8\xd1\x82\xd0\xb5 \xd0\xb3\xd0\xbe\xd0\xb4', null=True, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd0\xbe\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd1\x8b:')),
                ('sostav', models.FileField(help_text=b'3 \xd0\x9b\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbb\xd1\x8c \xd0\x90\xd1\x80\xd1\x88\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xbd 11.04.1993', upload_to=b'', verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbf\xd0\xb8\xd1\x88\xd0\xb8\xd1\x82\xd0\xb5 \xd1\x81\xd0\xbf\xd0\xb8\xd1\x81\xd0\xbe\xd0\xba \xd0\xb8\xd0\xb3\xd1\x80\xd0\xbe\xd0\xba\xd0\xbe\xd0\xb2. \xd0\x9e\xd0\xb4\xd0\xbd\xd0\xb0 \xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd1\x87\xd0\xba\xd0\xb0 - \xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbd \xd0\xb8\xd0\xb3\xd1\x80\xd0\xbe\xd0\xba.\xd0\xa1\xd0\xbe\xd0\xb1\xd0\xbb\xd1\x8e\xd0\xb4\xd0\xb0\xd0\xb9\xd1\x82\xd0\xb5 \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82 \xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xbe\xd0\xba - \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0 \xd0\xb0\xd0\xb2\xd1\x82\xd0\xbe\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f.')),
                ('regl', models.BooleanField(default=True)),
                ('first_league', models.BooleanField(default=True, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb0\xd1\x8f \xd0\xbb\xd0\xb8\xd0\xb3\xd0\xb0 \xd0\x90\xd0\x94\xd0\xa4\xd0\xa1 2016')),
                ('pokal', models.BooleanField(default=True, verbose_name=b'\xd0\x9a\xd1\x83\xd0\xb1\xd0\xbe\xd0\xba \xd0\x90\xd0\x94\xd0\xa4\xd0\xa1 2016')),
                ('winter_pokal', models.BooleanField(default=True, verbose_name=b'\xd0\x97\xd0\xb8\xd0\xbc\xd0\xbd\xd0\xb8\xd0\xb9 \xd0\xba\xd1\x83\xd0\xb1\xd0\xbe\xd0\xba \xd0\x90\xd0\x94\xd0\xa4\xd0\xa1 2015/16')),
            ],
        ),
    ]
