from django.contrib import admin

from .models import Contact, Notification, Certificate


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone_number') 
    list_display_links = ('first_name', 'email', 'phone_number')


@admin.register(Notification)
class NotificationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user_id', 'viewed')
    prepopulated_fields = {"slug": ("title",)} 
    list_display_links = ('title',)
    list_filter = ('user_id',) 


@admin.register(Certificate)
class CertificateModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_id', 'user_id') 
    list_display_links = ('course_id', 'user_id')
    list_filter = ('course_id', 'user_id',) 

