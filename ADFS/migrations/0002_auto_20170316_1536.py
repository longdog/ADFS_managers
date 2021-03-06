# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-16 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADFS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attention',
            name='avatar',
            field=models.ImageField(null=True, upload_to='', verbose_name='Эмблема команды:'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='first_league',
            field=models.BooleanField(default=True, verbose_name='Первая лига АДФС 2016'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='grundung',
            field=models.DateField(help_text='Если ваша команда была основана ранее, укажите год', null=True, verbose_name='Год основания команды:'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='name',
            field=models.CharField(max_length=40, null=True, verbose_name='Имя и Фамилия:'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='phone',
            field=models.CharField(max_length=12, null=True, verbose_name='Контактный телефон для связи:'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='pokal',
            field=models.BooleanField(default=True, verbose_name='Кубок АДФС 2016'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='sostav',
            field=models.FileField(help_text='3 Лионель Аршавин 11.04.1993', upload_to='', verbose_name='Напишите список игроков. Одна строчка - один игрок.Соблюдайте формат заявок - обработка автоматическая.'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='team',
            field=models.CharField(max_length=10, null=True, verbose_name='Название команды:'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='vkLink',
            field=models.CharField(max_length=40, null=True, verbose_name='Ссылка на ваш профиль в вк:'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='winter_pokal',
            field=models.BooleanField(default=True, verbose_name='Зимний кубок АДФС 2015/16'),
        ),
    ]
