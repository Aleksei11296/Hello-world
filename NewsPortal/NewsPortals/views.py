from django.shortcuts import render
from datetime import *
from django.views.generic import ListView, DetailView
from .models import Post
from pprint import pprint


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # # Поле, которое будет использоваться для сортировки объектов
    # queryset = Post.objects.filter(
    #     rating__lt= 2
    # ).order_by(
    #     'heading'
    # )
    ordering = 'heading'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'post.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'post'
    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context["time_now"] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = 'Новый пост в среду!'
        return context


class PostsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — post.html
    template_name = 'posts.html'
    # Название объекта, в котором будет выбранный пользователем post
    context_object_name = 'posts'