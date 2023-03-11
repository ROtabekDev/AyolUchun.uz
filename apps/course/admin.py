from django.contrib import admin

from .models import Category_for_course, Course, Section, Episode

@admin.register(Category_for_course)
class CategoryForCourseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    prepopulated_fields = {"slug": ("title",)} 
    list_display_links = ('title',) 


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category_id', 'author', 'price')
    prepopulated_fields = {"slug": ("title",)} 
    list_display_links = ('title', 'category_id')
    list_filter = ('category_id',) 

@admin.register(Section)
class SectionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'section_title', 'course_id', 'section_type', 'is_public')
    list_display_links = ('section_title', 'course_id')
    list_filter = ('section_type',) 

@admin.register(Episode)
class EpisodeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'length', 'section_id')
    list_display_links = ('title',)   

