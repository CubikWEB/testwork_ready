# Generated by Django 4.0.1 on 2022-01-25 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testworkapp', '0007_alter_comment_date_alter_newslist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 25, 11, 50, 46, 769152), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 25, 11, 50, 46, 767154), verbose_name='Дата создания'),
        ),
    ]