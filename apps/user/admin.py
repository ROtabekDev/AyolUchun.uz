from django.contrib import admin

from .models import (
    User, UserProfile, Purchased_course, 
    Country, Region, Speciality
    )

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Purchased_course)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Speciality)
