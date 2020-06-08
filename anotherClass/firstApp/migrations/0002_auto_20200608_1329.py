# Generated by Django 3.0.5 on 2020-06-08 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='class',
            name='like_user',
            field=models.ManyToManyField(related_name='like_class', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classanswer',
            name='inClass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='anw_class', to='firstApp.Class'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='date',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='firstApp.ClassDate'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='inClass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='firstApp.Class'),
        ),
        migrations.AlterField(
            model_name='class',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to='class'),
        ),
        migrations.AlterField(
            model_name='class',
            name='tutor_photo',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to='tutor'),
        ),
    ]
