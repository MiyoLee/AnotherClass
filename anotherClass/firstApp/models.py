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
    category = models.ForeignKey('firstApp.Category', on_delete=models.CASCADE, default=2)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    views = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ['-id']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('firstApp.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class Level(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Mode(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Class(models.Model):
    title = models.CharField(max_length=50)
    tutor = models.CharField(max_length=10)
    tutor_photo = models.ImageField(upload_to="tutor", default='')
    tutor_insta = models.CharField(null=True, blank=True, max_length=50, default='')
    tutor_blog = models.CharField(null=True, blank=True, max_length=50, default='')
    tutor_youtube = models.CharField(null=True, blank=True, max_length=50, default='')
    category = models.ForeignKey('firstApp.Category', on_delete=models.CASCADE, default=1, related_name='category')
    area = models.ForeignKey('firstApp.Area', on_delete=models.CASCADE, default=1)
    photo = models.ImageField(upload_to="class")
    body = RichTextUploadingField(default='')
    tutor_body = RichTextUploadingField(default='')
    price = models.PositiveIntegerField(null=True)
    time = models.PositiveIntegerField(null=True)
    level = models.ForeignKey('firstApp.Level', on_delete=models.CASCADE, default=1, related_name='level')
    mode = models.ForeignKey('firstApp.Mode', on_delete=models.CASCADE, default=1, related_name='mode')
    in_min = models.PositiveIntegerField(null=True, blank=True, default='1')
    in_max = models.PositiveIntegerField(null=True, blank=True, default='1')

class ClassReview(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    inClass = models.ForeignKey('firstApp.Class', on_delete=models.CASCADE, default=1, related_name='review_class')
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class ClassQna(models.Model):
    question = models.TextField()
    answer = models.TextField(null=True, blank=True, default='등록된 답변이 없습니다.')
    inClass = models.ForeignKey('firstApp.Class', on_delete=models.CASCADE, default=1, related_name='qna_class')
    created_date = models.DateTimeField(default=timezone.now)
    answer_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.question

class State(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Education(models.Model):
    university = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    inClass = models.ForeignKey('firstApp.Class', on_delete=models.CASCADE, default=1, related_name='edu_class')
    state = models.ForeignKey('firstApp.State', on_delete=models.CASCADE, default=1, related_name='state')

class Certificate(models.Model):
    inClass = models.ForeignKey('firstApp.Class', on_delete=models.CASCADE, default=1, related_name='certi_class')
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ClassDate(models.Model):
    inClass = models.ForeignKey('firstApp.Class', on_delete=models.CASCADE, default=1, related_name='date_class')
    date = models.DateTimeField(default=timezone.now)