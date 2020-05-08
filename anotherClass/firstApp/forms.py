from django import forms
from .models import Post,Comment, ClassQna
from .models import Class
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import ModelForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['category', 'title', 'text']

        widgets = {
                    'title': forms.TextInput(
                        attrs={'class': 'form-control', 'style': 'width:835px; position:relative; left:8.9%; margin:0;',
                               'placeholder': '제목을 입력하세요.'}
                    ),
                    'text': forms.CharField(widget=CKEditorUploadingWidget()),
                }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'style': 'margin:0; display:inline-block; width:90%; height:100px;'})
        }


class QuestionForm(forms.ModelForm):

    class Meta:
        model = ClassQna
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 100%; height:10%; resize:none;'})
        }




class CreateClass(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['title', 'tutor', 'tutor_photo', 'tutor_insta', 'tutor_blog', 'tutor_youtube', 'category', 'area',
                  'photo', 'body', 'tutor_body', 'price', 'time', 'in_min', 'in_max', 'level', 'mode']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 75%', 'placeholder': '제목을 입력하세요.'}
            ),
            'tutor': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 30%', 'placeholder': '이름을 입력하세요.'},
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
            'tutor_body': forms.CharField(widget=CKEditorUploadingWidget()),

        }

class SignupForm(ModelForm):
    비밀번호_확인 = forms.CharField(max_length=200, widget=forms.PasswordInput())

    field_order=['username','password','비밀번호_확인','last_name','first_name','email']

    class Meta:
        model=User
        widgets = {'password':forms.PasswordInput}
        fields = ['username','password','last_name','first_name','email']
