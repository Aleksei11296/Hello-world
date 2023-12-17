from django.contrib import admin
from .models import Post, CustomUser, Reply, Category

admin.site.register(Post)
admin.site.register(CustomUser)
admin.site.register(Reply)
admin.site.register(Category)


