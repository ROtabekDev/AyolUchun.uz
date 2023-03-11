from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from django.core.files.base import File
 
from .models import User, UserProfile, Completed_course 

from apps.main.models import Certificate

from helpers.generate_pdf import generate_certificate


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


@receiver(post_save, sender=Completed_course)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_name = f"{instance.user_id.first_name} {instance.user_id.last_name}" 
        course_name = instance.course_id.title
        
        generate_certificate(user_name=user_name, course_name=course_name, completed_course_id=instance.id)
        
        file_path =f"media/main/certificate/file/{user_name}_{course_name}_{instance.id}.pdf"
        
        Certificate.objects.create(course_id=instance.course_id, user_id=instance.user_id)
        certificate = Certificate.objects.filter(course_id=instance.course_id, user_id=instance.user_id)[0]

        certificate.file = file_path
        certificate.save()
        