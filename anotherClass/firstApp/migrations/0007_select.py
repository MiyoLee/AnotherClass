# Generated by Django 3.0.5 on 2020-06-01 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0006_merge_20200601_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Select',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstApp.Area')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstApp.Category')),
            ],
        ),
    ]
