from django import forms
from .models import Post
from .models import Class
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'text']

        widgets = {
                    'title': forms.TextInput(
                        attrs={'class': 'form-control', 'style': 'width: 75%', 'placeholder': '제목을 입력하세요.'}
                    ),
                    'text': forms.CharField(widget=CKEditorUploadingWidget()),
                }

class CreateClass(forms.ModelForm):
    class Meta:
        model = Class

        fields = ['title', 'tutor', 'body', 'photo']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'tutor': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 30%', 'placeholder': '이름을 입력하세요.'},
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }
