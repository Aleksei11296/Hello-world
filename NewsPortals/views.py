from django.shortcuts import render, get_object_or_404
from datetime import *
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from .models import Post, BaseRegisterForm
from .filters import PostFilter
from pprint import pprint
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Category


class Post_List(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'post'

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['filterset'] = self.filterset
        return context


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
    paginate_by = 10  # вот так мы можем указать количество записей на странице

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['filterset'] = self.filterset
        return context


class PostsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — post.html
    template_name = 'posts.html'
    # Название объекта, в котором будет выбранный пользователем post
    context_object_name = 'posts'


# Добавляем новое представление для создания товаров.

class PostUpdate(PermissionRequiredMixin, UpdateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'create.html'
    permission_required = ('NewsPortals.change_post',)


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class CreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'create.html'
    context_object_name = 'news'
    permission_required = ('NewsPortals.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/post/article/create/':
            post.type = 'A'
        post.save()
        return super().form_valid(form)


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'prodected_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = reverse_lazy('post_list')


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/post/search/')


class CatigoryView(Post_List):
    model = Post
    template_name = 'category_view.html'
    context_object_name = 'category_view'

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.category = None

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-category_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы подписались!'
    return render(request, 'subscribe.html', {'category': category, 'message': message})
