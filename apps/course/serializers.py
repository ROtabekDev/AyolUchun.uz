from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category_for_course


class CategoryForCourseListSerializer(ModelSerializer):

    class Meta:
        model = Category_for_course
        fields = ('id', 'title',)