from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator,MinValueValidator

from helpers.models import BaseModel

from mutagen.mp4 import MP4, MP4StreamInfoError


 
class Category_for_course(BaseModel):
    """Kurslar uchun kategoriya"""
    title = models.CharField('Sarlavhasi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Course(BaseModel):
    """Kurslar uchun model"""

    COURSE_TYPE = (
        ('Bestseller', 'Ko`p sotilgan'),
        ('Recommended', 'Tavsiya etiladi'),
        ('Nothing', 'Oddiy'),
    )

    title = models.CharField('Kurs nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)
    category_id = models.ForeignKey(Category_for_course, on_delete=models.CASCADE)
    desciption = models.TextField('Kurs haqida ma`lumot')
    slider = models.ImageField('Rasm', upload_to='course/course/slider/')
    author = models.CharField('Muallif', max_length=150)
    type = models.CharField('Kurs turi', choices=COURSE_TYPE, max_length=15, default='Nothing')
    price = models.DecimalField('Narxi', max_digits=12, decimal_places=2)
    is_discount = models.BooleanField('Chegirma', default=False)
    discount_price = models.DecimalField('Chegirmadagi narxi', max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'


class Section(BaseModel):
    """Bo`limlar uchun model"""

    SECTION_TYPE = (
        ('Not seen', 'Ko`rilmagan'),
        ('In progress', 'Jarayonda'),
        ('Reviewed', 'Ko`rilgan'),
    )

    section_title = models.CharField('Sarlavhasi', max_length=150)
    section_number = models.PositiveIntegerField('Tartib nomeri', default=1)
    section_type = models.CharField('Bo`lim turi', choices=SECTION_TYPE, default='Not seen', max_length=20)
    is_public = models.BooleanField(default=False)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.section_number}. {self.section_title}"
    
    class Meta:
        verbose_name = 'Bo`lim'
        verbose_name_plural = 'Bo`limlar'

class Episode(BaseModel):
    """Videolar uchun model"""
    title = models.CharField('Nomi', max_length=150)
    file = models.FileField('Fayl', upload_to='course/episode/file/')
    place_number = models.PositiveIntegerField('Tartib nomeri', default=1)
    length = models.DecimalField(max_digits=100,decimal_places=2, blank=True, null=True, default=0)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)

    def get_video_length(self):
        try:
            video=MP4(self.file)
            return video.info.length
            
        except MP4StreamInfoError:
            return 0.0 
    
  
    def save(self,*args, **kwargs):
        self.length=self.get_video_length()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Epizod'
        verbose_name_plural = 'Epizodlar'


class Episode_viewed(BaseModel):
    """Video ko`rilganligi"""
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    episode_id = models.ForeignKey(Episode, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.episode_id.title
    
    class Meta:
        verbose_name = 'Video ko`rilganligi'
        verbose_name_plural = 'Video ko`rilganligi'
        

class Purchased_course(BaseModel):
    """Sotib olingan kurslar"""
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Kurs')
    
    def __str__(self):
        return f'User: {self.user_id.phone_number}. Kurs: {self.course_id.title}'

    class Meta:
        verbose_name = 'Sotib olingan kurs'
        verbose_name_plural = 'Sotib olingan kurslar'


class Completed_course(BaseModel):
    """Tugatilgan kurslar"""
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Kurs')
    
    def __str__(self):
        return f'User: {self.user_id.phone_number}. Kurs: {self.course_id.title}'

    class Meta:
        verbose_name = 'Tugatilgan kurs'
        verbose_name_plural = 'Tugatilgan kurslar'


class Course_completion(BaseModel):
    """Kurs uchun xulosa"""
    completed_course = models.ForeignKey(Completed_course, on_delete=models.CASCADE, verbose_name='Tugatilgan kurs')
    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    # course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Kurs')
    rate_number = models.PositiveIntegerField('Reyting qiymati', validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    message = models.CharField('Xabar', max_length=250)

    def __str__(self):
        return f'User: {self.completed_course.user_id.phone_number}. Kurs: {self.completed_course.course_id.title}. Baho: {self.rate_number}.'
    
    class Meta:
        verbose_name = 'Kurs uchun xulosa'
        verbose_name_plural = 'Kurs uchun xulosalar'

class Video_comment(BaseModel):
    """Izohlar"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Muallif')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Asosiy izoh', blank=True, null=True)
    episode_id = models.ForeignKey(Episode, on_delete=models.CASCADE, verbose_name='Video')
    text = models.TextField(verbose_name='Izoh matni')
    is_child = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) 

    class Meta:
        verbose_name = 'Izoh'   
        verbose_name_plural = 'Izohlar'   