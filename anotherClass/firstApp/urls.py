from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.blogMain, name='main'),
    path('class/', views.categoryselect, name='class'),
    path('product/', views.product, name='product'),
    path('apply/', views.apply, name='apply'),
    path('createpost/', views.createpost, name='createpost'),
    path('createclass/', views.createclass, name='createclass'),
    path('community/', views.community, name='community'),
    path('login/', views.login, name='login'),
    path('community/<int:pk>/', views.post_detail, name='post_detail'),
    path('community/<int:pk>/update', views.update_post, name='update_post'),
    path('community/<int:pk>/delete', views.delete_post, name='delete_post'),
]