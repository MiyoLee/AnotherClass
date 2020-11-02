from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django_filters.views import FilterView
from .filters import ClassFilter


urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.blogMain, name='main'),
    path('class_search/', views.class_search, name='class_search'),
    path('class_align/', views.class_align, name='class_align'),
    path('product/<int:class_id>/', views.product, name='product'),
    path('product/<int:pk>/remove', views.product_remove, name='product_remove'),
    path('product/<int:class_id>/like/', views.like, name='like'),
    path('product/<int:class_id>/update', views.update_class, name='update_class'),
    path('product/<int:class_id>/sale', views.classSale, name='classSale'),
    path('product/<int:class_id>/apply/', views.apply, name='apply'),
    path('product/<int:pk>/create_answer/', views.create_answer, name='create_answer'),
    path('product/<int:pk>/update_answer/', views.update_answer, name='update_answer'),
    path('createpost/', views.createpost, name='createpost'),
    path('intro_createclass/', views.intro_createclass, name='intro_createclass'),
    path('createclass/', views.createclass, name='createclass'),
    path('createclass/<int:class_id>/complete/', views.create_complete, name='create_complete'),
    path('product/<int:class_id>/apply/apply_complete', views.apply_complete, name='apply_complete'),
    path('createclass/<int:class_id>/addTime/', views.addTime, name='addTime'),
    path('createclass/<int:class_id>/addTutor/', views.addTutor, name='addTutor'),
    path('createclass/addTime/<int:pk>/time/remove', views.time_remove, name='time_remove'),
    path('createclass/addTutor/<int:pk>/certi/remove', views.certi_remove, name='certi_remove'),
    path('createclass/addTutor/<int:pk>/edu/remove', views.edu_remove, name='edu_remove'),
    path('community/', views.community, name='community'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('intro_delete/', views.intro_delete, name='intro_delete'),
    path('delete/', views.delete, name='delete'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage/myClass/', views.myClass, name='myClass'),
    path('mypage/permit/', views.permit, name='permit'),
    path('mypage/permit/<int:pk>/remove', views.class_permit, name='class_permit'),
    path('mypage/myClass/<int:class_id>/applicant', views.applicant, name='applicant'),
    path('mypage/myApply/', views.myApply, name='myApply'),
    path('mypage/myApply/<int:pk>/cancel', views.cancelApply, name='cancelApply'),
    path('mypage/myApply/<int:class_id>/review', views.review, name='review'),
    path('mypage/mylike/', views.mylike, name='mylike'),
    path('mypage/sybermoney/', views.sybermoney, name='sybermoney'),
    path('mypage/member_info_management/', views.member, name='member_info_management'),
    path('change_pw/', views.change_pw, name='change_pw'),
    path('community/best/', views.bestPost, name='bestPost'),
    path('community/myPost/', views.myPost, name='myPost'),
    path('community/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('community/<int:pk>/update', views.update_post, name='update_post'),
    path('community/<int:pk>/delete', views.delete_post, name='delete_post'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('community/<int:pk>/post_recommend', views.recommend, name='post_recommend'),
    path('community/<int:pk>/post_no_recommend', views.no_recommend, name='post_no_recommend'),
    path('community/<int:pk>/comment_remove', views.comment_remove, name='comment_remove'),
    path('community/<int:pk>/comment_update', views.comment_update, name='comment_update'),
    path('community/<int:pk>/create_ccomment', views.create_ccomment, name='create_ccomment'),
    path('community/<int:pk>/remove_ccomment', views.remove_ccomment, name='remove_ccomment'),
    path('community/<int:pk>/update_ccomment', views.update_ccomment, name='update_ccomment'),
    path('search/', views.searchResult, name='searchResult'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
