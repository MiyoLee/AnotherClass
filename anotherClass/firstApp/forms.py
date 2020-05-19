from django import forms
from .models import Post,Comment, ClassQna, Class, Apply, ClassDate, Certificate, Education
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

class AddTime(forms.ModelForm):
    class Meta:
        model = ClassDate
        fields = ['date']
        widgets = {

        }
class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={'style': 'width: 40%', 'placeholder': ' 토익 100점 , HSK 8급 , 컴퓨터활용능력 3급 . . .'}
            )

        }
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['university', 'department', 'state']
        widgets = {
            'university': forms.TextInput(
                attrs={'style': 'width: 17%', 'placeholder': ' 서울대학교 '}
            ),
            'department': forms.TextInput(
                attrs={'style': 'width: 17%', 'placeholder': ' 실용음악과'}
            )
            

        }

class CreateClass(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['title', 'tutor', 'tutor_photo', 'category', 'area', 'photo', 'body',
                  'in_min', 'in_max', 'tutor_body', 'price', 'time', 'level', 'mode', 'tutor_insta', 'tutor_blog', 'tutor_youtube']

        widgets = {
            'title': forms.TextInput(
                attrs={'style': 'width: 350%', 'placeholder': '제목을 입력하세요.'}
            ),
            'tutor': forms.TextInput(
                attrs={'style': 'width: 170%', 'placeholder': '이름을 입력하세요.'},
            ),
            'tutor_insta': forms.TextInput(
                attrs={'style': 'width: 300%', 'placeholder': '@instagram'},
            ),
            'tutor_blog': forms.TextInput(
                attrs={'style': 'width: 300%', 'placeholder': 'https://blog.naver.com/AnotherClass'},
            ),
            'tutor_youtube': forms.TextInput(
                attrs={'style': 'width: 300%', 'placeholder': '어나더클래스 , youtube.com/AnotherClass'},
            ),

            'price': forms.NumberInput(
                attrs={'style': 'width: 100px'},
            ),
            'time': forms.NumberInput(
                attrs={'style': 'width: 100px'},
            ),
            'in_min': forms.NumberInput(
                attrs={'style': 'width: 70px'},
            ),
            'in_max': forms.NumberInput(
                attrs={'style': 'width: 70px'},
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
            'tutor_body': forms.CharField(widget=CKEditorUploadingWidget()),

        }

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'number', 'text']

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 30%', 'placeholder': 'ex)홍길동'},
            ),
            'number': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 30%', 'placeholder': 'ex)010-1234-5678'},
            ),
            'text': forms.CharField(widget=CKEditorUploadingWidget()),
        }

class SignupForm(ModelForm):
    password_확인 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs = {'placeholder': '필수 입력'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs = {'placeholder': '필수 입력'}))
    username = forms.CharField(widget=forms.TextInput(attrs = {'placeholder': '필수 입력'}))
    field_order=['username','password','password_확인','last_name','first_name','email']


    class Meta:
        model=User
        widgets = {'password':forms.PasswordInput}
        
        fields = ['username','password','last_name','first_name','email']
