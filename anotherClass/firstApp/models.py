from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

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

class Bullet(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey('firstApp.Category', on_delete=models.CASCADE, default=2)
    bullet = models.ForeignKey('firstApp.Bullet', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=60)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    recommendations = models.PositiveIntegerField(default=0)
    recommend_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recommend_post')
    no_recommendations = models.PositiveIntegerField(default=0)
    no_recommend_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='no_recommend_post')

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
    text = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['id']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class CComment(models.Model):
    post = models.ForeignKey('firstApp.Post', on_delete=models.CASCADE, related_name='ccomments', default=1)
    parent_comment = models.ForeignKey('firstApp.Comment', on_delete=models.CASCADE, related_name='child_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    text = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)

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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    tutor = models.CharField(max_length=10)
    tutor_photo = ProcessedImageField(upload_to="tutor", processors=[ResizeToFill(300,300)], default='')
    tutor_insta = models.CharField(null=True, blank=True, max_length=50, default='')
    tutor_blog = models.CharField(null=True, blank=True, max_length=50, default='')
    tutor_youtube = models.CharField(null=True, blank=True, max_length=50, default='')
    category = models.ForeignKey('firstApp.Category', on_delete=models.CASCADE, default=1, related_name='category')
    area = models.ForeignKey('firstApp.Area', on_delete=models.CASCADE, default=1)
    photo = ProcessedImageField(upload_to="class", processors=[ResizeToFill(600,450)], default='')
    body = RichTextUploadingField(default='')
    tutor_body = RichTextUploadingField(default='')
    price = models.CharField(max_length=10)
    time = models.CharField(max_length=5)
    level = models.ForeignKey('firstApp.Level', on_delete=models.CASCADE, default=1, related_name='level')
    mode = models.ForeignKey('firstApp.Mode', on_delete=models.CASCADE, default=1, related_name='mode')
    in_min = models.PositiveIntegerField(null=True, blank=True, default='1')
    in_max = models.PositiveIntegerField(null=True, blank=True, default='1')
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_class')
    like_count = models.PositiveIntegerField(default=0)
    on_sale = models.BooleanField(null=True, default=False)
    sale_price = models.CharField(null=True, max_length=10)
    def __str__(self):
        return self.title



class Apply(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    inClass = models.ForeignKey('firstApp.Class', on_delete=models.CASCADE, default=1, related_name='apply')
    date = models.ForeignKey('firstApp.ClassDate', on_delete=models.CASCADE, default=1, related_name='apply')
    name = models.CharField(max_length=10)
    number = models.CharField(max_length=13)
    text = RichTextUploadingField(default='')
    def __str__(self):
        return self.name

class ClassReview(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    inClass = models.ForeignKey('firstApp.Class', on_delete=models.CASCADE, default=1, related_name='review_class')
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class ClassQna(models.Model):
    question = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    inClass = models.ForeignKey('firstApp.Class', on_delete=models.CASCADE, default=1, related_name='qna_class')
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.question

class ClassAnswer(models.Model):
    answer = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    inClass = models.ForeignKey('firstApp.Class', on_delete=models.CASCADE, default=1, related_name='anw_class')
    inQuestion = models.ForeignKey('firstApp.ClassQna', on_delete=models.CASCADE, default=1, related_name='answer_class')
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.answer

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
