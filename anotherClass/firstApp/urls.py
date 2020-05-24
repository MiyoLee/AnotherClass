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
    path('product/<int:class_id>/update', views.update_class, name='update_class'),
    path('product/<int:class_id>/apply/', views.apply, name='apply'),
    path('createpost/', views.createpost, name='createpost'),
    path('createclass/', views.createclass, name='createclass'),
    path('createclass/<int:class_id>/addTime/', views.addTime, name='addTime'),
    path('createclass/<int:class_id>/addTutor/', views.addTutor, name='addTutor'),
    path('createclass/<int:class_id>/updateTime/', views.update_time, name='update_time'),
    path('createclass/addTime/<int:pk>/time/remove', views.time_remove, name='time_remove'),
    path('community/', views.community, name='community'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage/myClass/', views.myClass, name='myClass'),
    path('mypage/myApply/', views.myApply, name='myApply'),
    path('change_pw/', views.change_pw, name='change_pw'),
    path('community/myPost/', views.myPost, name='myPost'),
    path('community/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('community/<int:pk>/update', views.update_post, name='update_post'),
    path('community/<int:pk>/delete', views.delete_post, name='delete_post'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('community/<int:pk>/comment_remove', views.comment_remove, name='comment_remove'),
    path('community/<int:pk>/comment_update', views.comment_update, name='comment_update'),
    path('community/<int:pk>/create_ccomment', views.create_ccomment, name='create_ccomment'),
    path('community/<int:pk>/remove_ccomment', views.remove_ccomment, name='remove_ccomment'),
    path('community/<int:pk>/update_ccomment', views.update_ccomment, name='update_ccomment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
