from django.contrib import admin

from .models import (
    User, UserProfile, Purchased_course, 
    Country, Region, Speciality, Completed_course
    )


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'email')
    list_display_links = ('first_name', 'last_name') 


@admin.register(UserProfile)
class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'birthday', 'country_id', 'region_id')
    list_display_links = ('user',) 


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


@admin.register(Country)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    prepopulated_fields = {"slug": ("name",)} 
    list_display_links = ('name',) 


@admin.register(Region)
class RegionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_id', 'name')
    prepopulated_fields = {"slug": ("name",)} 
    list_display_links = ('country_id', 'name')
    list_filter = ('country_id',) 


@admin.register(Speciality)
class SpecialityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    prepopulated_fields = {"slug": ("title",)} 
    list_display_links = ('title',)
