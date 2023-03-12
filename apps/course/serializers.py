from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category_for_course, Course, Section, Episode, Course_completion, Video_comment

from django.db.models import Sum

class CategoryForCourseListSerializer(ModelSerializer):

    class Meta:
        model = Category_for_course
        fields = ('id', 'title',)

class CourseListSerializer(ModelSerializer):
    category_id = serializers.StringRelatedField()
    ranking = serializers.DecimalField(max_digits=2, decimal_places=1, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'category_id', 'slider', 'author', 'type', 'price', 'is_discount', 'discount_price', 'ranking')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
  
        if representation['is_discount'] == False:
            del representation['is_discount']
            del representation['discount_price']

        count_ranking = Course_completion.objects.filter(course_id=representation['id']).count()
        sum_ranking = Course_completion.objects.filter(course_id=representation['id']).aggregate(Sum('rate_number'))['rate_number__sum']
        
        if sum_ranking==None:
            sum_ranking=0 
            
        try:
            ranking = sum_ranking/count_ranking
        except ZeroDivisionError:
            ranking=0

        ranking = round(ranking, 1)
        
        representation['ranking']=ranking
        
        return representation