from django.contrib import admin

from .models import (
    Category_for_course, Course, Section, 
    Episode, Purchased_course, Completed_course, Course_completion, Video_comment
)

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

@admin.register(Purchased_course)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'course_id') 
    list_display_links = ('user_id', 'course_id')
    list_filter = ('user_id', 'course_id') 


@admin.register(Completed_course)
class CompletedCourseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'course_id') 
    list_display_links = ('user_id', 'course_id')
    list_filter = ('user_id', 'course_id')  

@admin.register(Course_completion)
class CourseCompletionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'completed_course', 'rate_number') 
    list_display_links = ('completed_course', 'rate_number')
    list_filter = ('completed_course',) 

@admin.register(Video_comment)
class VideoCommentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'parent', 'text', 'is_child') 
    list_display_links = ('user', 'text')
    list_filter = ('user',) 