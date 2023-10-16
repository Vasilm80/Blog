from django.contrib import admin

from blog.models import Post, Category, Coments

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
