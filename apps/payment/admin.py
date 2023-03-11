from django.contrib import admin

from .models import Payment

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'course_id', 'price', 'payment_status')
    list_display_links = ('user_id', 'course_id')
    list_filter = ('user_id', 'course_id') 

