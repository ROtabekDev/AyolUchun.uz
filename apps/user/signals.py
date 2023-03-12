from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import User, UserProfile 


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created: 
        UserProfile.objects.create(
                user = instance
            ) 

@receiver(post_delete, sender=UserProfile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete() 

        