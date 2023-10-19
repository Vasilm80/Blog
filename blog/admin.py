from django.contrib import admin

from blog.models import Post, Category, UserModel

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserModel)
