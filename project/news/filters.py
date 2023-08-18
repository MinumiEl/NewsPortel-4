import django_filters
from django_filters import FilterSet
from .models import Post, Category
from django import forms


class PostFilter(FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Заголовок',
                                      widget=forms.TextInput(attrs={'placeholder': 'Поиск по названию'}))
    postCategory = django_filters.ModelChoiceFilter(field_name='postCategory', empty_label='Все категории',
                                                    label='Категория', queryset=Category.objects.all())
    dateCreation = django_filters.DateFilter(field_name='dateCreation', lookup_expr='gte', label='Дата',
                                             widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        fields = ['title',
                  'postCategory',
                  'dateCreation']
