# Generated by Django 3.0.4 on 2020-05-12 06:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_auto_20200512_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 12, 6, 2, 0, 692565, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 12, 6, 2, 0, 632336, tzinfo=utc)),
        ),
    ]