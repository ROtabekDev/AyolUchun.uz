from django.contrib import admin

from .models import Blog, Category_for_blog, Views


@admin.register(Category_for_blog)
class CategoryForBlogModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('title',) 


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author') 
    list_display_links = ('title',)
    list_filter = ('category_id',) 

 
