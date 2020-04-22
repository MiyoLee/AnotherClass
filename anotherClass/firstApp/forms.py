from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ['title', 'author', 'text']

