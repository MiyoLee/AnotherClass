from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
from .models import Category
from .models import Classes

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Classes)