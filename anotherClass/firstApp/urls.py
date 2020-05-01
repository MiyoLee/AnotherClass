from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.blogMain, name='main'),
    path('class/', views.categoryselect, name='class'),
    path('product/<int:class_id>/', views.product, name='product'),
    path('apply/', views.apply, name='apply'),
    path('createpost/', views.createpost, name='createpost'),
    path('createclass/', views.createclass, name='createclass'),
    path('community/', views.community, name='community'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('community/category/<int:pk>/', views.post_category, name='post_category'),
    path('community/myPost/', views.myPost, name='myPost'),
    path('community/<int:pk>/', views.post_detail, name='post_detail'),
    path('community/<int:pk>/update', views.update_post, name='update_post'),
    path('community/<int:pk>/delete', views.delete_post, name='delete_post'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('community/<int:pk>/comment/remove', views.comment_remove, name='comment_remove'),
    path('community/<int:pk>/comment/update', views.comment_update, name='comment_update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
