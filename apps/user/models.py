from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

from django.core.validators import RegexValidator

from rest_framework_simplejwt.tokens import RefreshToken

from helpers.models import BaseModel
from apps.course.models import Course

class CustomUserManager(BaseUserManager):
    """Maxsus foydalanuvchi menejeri"""
    def create_user(self, first_name, last_name, phone_number,  password=None):  
        user = self.model( 
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, phone_number, password=None): 
        user = self.model(phone_number=phone_number, first_name=first_name,
                          last_name=last_name, password=make_password(password)) 
        user.is_superuser = True  
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """Foydalanuvchi uchun model"""
    first_name = models.CharField('Ism', max_length=100)
    last_name = models.CharField('Familiya', max_length=100)
    patronymic = models.CharField('Otasining ismi', max_length=100, blank=True, null=True)
    phone_number = models.CharField(
        "Telefon nomer", 
        max_length=15, 
        unique=True,
        error_messages={'unique': 'Bu telefon nomer ro`yhatdan o`tgan!'},
        validators=[RegexValidator(regex='^[+][998]{3}?[0-9]{9}$', message='Iltimos telefon nomerni to`g`ri kiriting')]
        )
    email = models.EmailField('Elektron pochta', unique=True, blank=True, null=True)
    email_is_approad = models.BooleanField('Elektron pochta holati', default=False)
    # paid_courses = models.ManyToManyField(Course, blank=True)
    # completed_courses = models.ManyToManyField(Course, blank=True)
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False)     

    USERNAME_FIELD = 'phone_number' 
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Barcha foydalanuvchilar'


    def __str__(self): 
        return self.phone_number
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
    
class Purchased_course(BaseModel):
    """Sotib olingan kurslar"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Kurs')
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f'User: {self.user_id.phone_number}. Kurs: {self.course_id.title}'

    class Meta:
        verbose_name = 'Sotib olingan kurs'
        verbose_name_plural = 'Sotib olingan kurslar'


class UserProfile(BaseModel):
    """Foydalanuvchi uchun profil modeli"""

    GENDER_TYPE = (
        ('Male', 'Erkak'),
        ('Female', 'Ayol')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    profile_pic = models.ImageField('Rasm', upload_to='user/user_profile/profile_pic/', default='media/user/user_profile/profile_pic/default-user-image.png')
    birthday = models.DateTimeField('Tug`ilgan sanasi', null=True, blank=True)
    gender = models.CharField('Jinsi', max_length=10, choices=GENDER_TYPE, null=True, blank=True)
    country_id = models.ForeignKey('Country', on_delete=models.SET_NULL, blank=True, null=True)
    region_id = models.ForeignKey('Region', on_delete=models.SET_NULL, blank=True, null=True)
    zip_code = models.PositiveIntegerField('Pochta indeksi', blank=True, null=True)
    address = models.CharField('Manzil', max_length=250, blank=True, null=True)
    facebook_profile = models.CharField('Facebook sahifa', max_length=150, null=True, blank=True)
    instagram_profile = models.CharField('Instagram sahifa', max_length=150, null=True, blank=True)
    imkon_profile = models.CharField('Imkon sahifa', max_length=150, null=True, blank=True)
    linkedin_profile = models.CharField('Linkedin sahifa', max_length=150, null=True, blank=True)
    telegram_profile = models.CharField('Telegram sahifa', max_length=150, null=True, blank=True)
    workplace = models.CharField('Ish joyi', max_length=250, null=True, blank=True)
    position = models.CharField('Lavozimi', max_length=150, null=True, blank=True)
    specialty = models.ForeignKey('Speciality', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField('Foydalanuvchi haqida ma`lumot', null=True, blank=True)


    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profillar'


    def __str__(self): 
        return self.user.phone_number
    

class Country(BaseModel):
    """Mamlakatlar"""
    name = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Mamlakat'
        verbose_name_plural = 'Mamlakatlar'


class Region(BaseModel):
    """Viloyatlar"""
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Mamlakat'
        verbose_name_plural = 'Mamlakatlar'

class Speciality(BaseModel):
    """Mutaxassislik"""
    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Mutaxassislik'
        verbose_name_plural = 'Mutaxassisliklar'


    
