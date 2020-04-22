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
]