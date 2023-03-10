from django.contrib import admin

from .models import Category_for_course, Course, Section, Episode

admin.site.register(Category_for_course)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Episode)

