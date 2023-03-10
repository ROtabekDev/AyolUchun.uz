from django.contrib import admin

from .models import Blog, Category_for_blog

admin.site.register(Blog)
admin.site.register(Category_for_blog)

