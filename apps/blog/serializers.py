from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Blog, Category_for_blog


class CategoryBlogSerializer(ModelSerializer):

    class Meta:
        model = Category_for_blog
        fields = ('id','title')


class BlogListSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ('title', 'slider', 'author', 'author_speciality', 'created_at')