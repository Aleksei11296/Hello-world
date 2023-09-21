from django_filters import FilterSet, DateFilter
from django import forms
from .models import Post

# Создаем свой набор фильтров для модели.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    in_post = DateFilter(field_name='in_post', widget=forms.DateInput(attrs={'type': 'date'}),
                         lookup_expr='date__gte')
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'heading': ['icontains'],
           # поиск по названию
           'author': ['exact'],
       }