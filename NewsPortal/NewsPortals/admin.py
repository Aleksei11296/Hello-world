from django.contrib import admin
from django.urls import path, include
from .models import *


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)
# Register your models here.
