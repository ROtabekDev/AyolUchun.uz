from django.db import models

from helpers.models import BaseModel

from apps.user.models import User

from ckeditor.fields import RichTextField


class Blog(BaseModel):
    """Maqolalar uchun model"""
    title = models.CharField('Sarlavhasi', max_length=250)
    slug = models.SlugField('Slugi', max_length=250)
    category_id = models.ForeignKey('Category_for_blog', on_delete=models.SET_NULL, null=True, blank=True)
    author = models.CharField('Muallif', max_length=150)
    author_speciality = models.CharField('Muallif kasbi', max_length=150)
    slider = models.ImageField('Rasm', upload_to='blog/blog/slider/')
    content = RichTextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class Category_for_blog(BaseModel):
    """Maqola uchun kategoriyalar modeli"""
    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Views(BaseModel):
    """Ko`rishlar soni"""
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    device_id = models.CharField('Qurilma manzili', max_length=250, null=True, blank=True)
    ip_address = models.CharField('Ip manzili', max_length=250, null=True, blank=True)

    def __str__(self):
        return self.blog_id.title
    
    class Meta:
        verbose_name = 'Ko`rishlar soni'
        verbose_name_plural = 'Ko`rishlar soni'
