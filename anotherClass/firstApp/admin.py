from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Post
from .models import PostAdmin
from .models import Comment
from .models import Category
from .models import Area
from .models import detailArea
from .models import Class

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Area)
admin.site.register(detailArea)
admin.site.register(Class)