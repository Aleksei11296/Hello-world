from django.contrib import admin
from django.urls import include
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# Импортируем созданное нами представление
from .views import PostList, PostsDetail, Post_List, CreateView, PostUpdate, PostDelete, ProtectedView, BaseRegisterView, upgrade_me, CatigoryView, subscribe


urlpatterns = [
   # path('admin/', admin.site.urls),
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view()),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostsDetail.as_view(), name='post_detail'),
   path('search/', Post_List.as_view(), name='post_list'),
   path('news/create/', CreateView.as_view(), name='news_create'),
   path('article/create/', CreateView.as_view(), name='article_create'),
   path('news/<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
   path('article/<int:pk>/update/', PostUpdate.as_view(), name='article_delete'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('article/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),
   path('prodected_page/', ProtectedView.as_view()),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('categories/<int:pk>', CatigoryView.as_view(), name='category_view'),
   path('categories/<int:pk>/subscribe',subscribe, name='subscribe')
]