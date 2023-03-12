from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from rest_framework.exceptions import AuthenticationFailed

from .models import (
    User, UserProfile, Country, Region, 
    Speciality, Purchased_course, 
)

from apps.course.models import Video_comment
from apps.main.models import Certificate

class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.DictField(source='tokens', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name',  'last_name', 'phone_number', 'password', 'password2', 'token')
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError({'success': False, 'message': 'Parollar bir xil emas.'})
        
        del password2

        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer): 
    phone_number = serializers.CharField(max_length=15) 
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True) 

    class Meta:
        model = User
        fields = ('id', 'first_name',  'last_name', 'phone_number', 'password', 'tokens')

    def validate(self, attrs): 
        phone_number = attrs.get('phone_number', '')
        password = attrs.get('password', '') 
        print(phone_number)
        print(password)

        user = authenticate(phone_number=phone_number, password=password) 
        print(user)
 
        if not user:
            raise AuthenticationFailed({
                'message': 'Telefon nomer yoki parol noto`g`ri yoki foydalanuvchi faol emas.'
            })

        return {
            "first_name": user.first_name, 
            "last_name": user.last_name, 
            'phone_number': user.phone_number, 
            'tokens': user.tokens
        } 


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic', 'phone_number', 'email', 'email_is_approad')
        

class UserDetailSerializer(ModelSerializer):
    user = UserSerializer()
    country_id = serializers.StringRelatedField()
    region_id = serializers.StringRelatedField()
    specialty = serializers.StringRelatedField() 

    class Meta:
        model = UserProfile
        fields = (
            'id', 'user', 'profile_pic', 'birthday', 
            'gender', 'country_id', 'region_id', 
            'zip_code', 'address', 'facebook_profile', 
            'instagram_profile', 'imkon_profile', 
            'linkedin_profile', 'telegram_profile', 
            'workplace', 'position', 'specialty', 
            'description'
            )
         
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        print(instance.user)
        courses = Purchased_course.objects.filter(user_id=instance.user).count() 
        comments = Video_comment.objects.filter(user=instance.user).count() 
        certificates = Certificate.objects.filter(user_id=instance.user).count()  

        representation['courses'] = courses
        representation['comments'] = comments
        representation['certificates'] = certificates

        return representation
    
class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name')


class RegionSerializer(ModelSerializer):
    country_id = CountrySerializer()

    class Meta:
        model = Region
        fields = ('id', 'name', 'country_id')


class SpecialitySerializer(ModelSerializer):

    class Meta:
        model = Speciality
        fields = ('id', 'title')



class UserProfileUpdateSerializer(ModelSerializer):
    user = UserSerializer()
    country_id = CountrySerializer()
    region_id = RegionSerializer()
    specialty = SpecialitySerializer() 

    class Meta:
        model = UserProfile
        fields = (
            'id', 'user', 'profile_pic', 'birthday', 
            'gender', 'country_id', 'region_id', 
            'zip_code', 'address', 'facebook_profile', 
            'instagram_profile', 'imkon_profile', 
            'linkedin_profile', 'telegram_profile', 
            'workplace', 'position', 'specialty', 
            'description'
            )