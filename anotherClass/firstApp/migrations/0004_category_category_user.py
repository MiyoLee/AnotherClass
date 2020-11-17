# Generated by Django 3.0.5 on 2020-11-11 06:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstApp', '0003_auto_20201102_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_user',
            field=models.ManyToManyField(blank=True, related_name='category_user', to=settings.AUTH_USER_MODEL),
        ),
    ]