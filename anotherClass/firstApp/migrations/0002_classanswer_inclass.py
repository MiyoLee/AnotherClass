# Generated by Django 3.0.4 on 2020-05-25 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classanswer',
            name='inClass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='anw_class', to='firstApp.Class'),
        ),
    ]