from django import forms
from .models import Class, Category
from django_filters import FilterSet, NumberFilter, ModelMultipleChoiceFilter

class ClassFilter(FilterSet):

    category = ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),  # 필터링 데이터
        widget=forms.CheckboxSelectMultiple  # 필터링 방법(CheckBox)
    )

    class Meta:
        model = Class
        fields = ['category', 'area', 'level']

