from django.contrib import admin

from .models import Contact, Notification, Certificate

admin.site.register(Contact)
admin.site.register(Notification)
admin.site.register(Certificate)
