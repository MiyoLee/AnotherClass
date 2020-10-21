from django.contrib import admin

# Register your models here.

from .models import Post
from .models import PostAdmin
from .models import Comment, CComment
from .models import Bullet
from .models import Category
from .models import Area
from .models import detailArea
from .models import Class
from .models import Level
from .models import Mode
from .models import ClassReview
from .models import ClassQna
from .models import ClassAnswer
from .models import State
from .models import Education
from .models import Certificate
from .models import ClassDate
from .models import Apply
from .models import Profile
from .models import Photo

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(CComment)
admin.site.register(Bullet)
admin.site.register(Category)
admin.site.register(Area)
admin.site.register(detailArea)
admin.site.register(Class)
admin.site.register(Level)
admin.site.register(Mode)
admin.site.register(ClassReview)
admin.site.register(ClassQna)
admin.site.register(ClassAnswer)
admin.site.register(State)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(ClassDate)
admin.site.register(Apply)
admin.site.register(Profile)
admin.site.register(Photo)