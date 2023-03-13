from django.db import models

from helpers.models import BaseModel

from apps.user.models import User
from apps.course.models import Course


class Contact(BaseModel):
    """Bog`lanish"""
    first_name = models.CharField('Ism', max_length=150)
    email = models.EmailField('Elektron pochta')
    phone_number = models.CharField('Telefon nomer', max_length=20)
    message = models.TextField('Xabar')

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'


class Notification(BaseModel):
    """Bildirishnoma uchun model"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Sarlavhasi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)
    message = models.TextField('Xabar')
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Bildirishnoma'
        verbose_name_plural = 'Bildirishnomalar'


class Certificate(BaseModel):
    """Sertifikat"""
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Kurs')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    file = models.FileField('Fayl', blank=True, null=True, upload_to='main/certificate/file/')

    def __str__(self):
        return self.user_id.phone_number
    
    class Meta:
        verbose_name = 'Sertifikat'
        verbose_name_plural = 'Sertifikatlar'