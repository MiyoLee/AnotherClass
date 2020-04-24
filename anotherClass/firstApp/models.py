from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Area(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class detailArea(models.Model):
    name = models.CharField(max_length=20)
    parentArea = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    views = models.PositiveIntegerField(default = 0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class Class(models.Model):
    title = models.CharField(max_length=20)
    tutor = models.CharField(max_length=10)
    body = RichTextUploadingField()
