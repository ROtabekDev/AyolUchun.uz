from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Blog, Category_for_blog, Views


class CategoryBlogSerializer(ModelSerializer):

    class Meta:
        model = Category_for_blog
        fields = ('id','title')


class BlogListSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ('title', 'slug', 'slider', 'author', 'author_speciality', 'created_at')


    def to_representation(self, instance):
        representation = super().to_representation(instance)

        view_count = Views.objects.filter(blog_id=instance).count()   

        representation['view_count'] = view_count 

        return representation
    

class BlogDetailSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ('title', 'slider', 'author', 'author_speciality', 'content')


    def to_representation(self, instance):
        representation = super().to_representation(instance)

        view_count = Views.objects.filter(blog_id=instance).count()   

        representation['view_count'] = view_count 

        return representation