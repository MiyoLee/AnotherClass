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
from .models import Level
from .models import Mode
from .models import ClassReview
from .models import ClassQna
from .models import State
from .models import Education
from .models import Certificate
from .models import ClassDate

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Area)
admin.site.register(detailArea)
admin.site.register(Class)
admin.site.register(Level)
admin.site.register(Mode)
admin.site.register(ClassReview)
admin.site.register(ClassQna)
admin.site.register(State)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(ClassDate)

