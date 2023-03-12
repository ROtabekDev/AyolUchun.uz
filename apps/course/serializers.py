from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category_for_course, Course, Section, Episode, Course_completion, Video_comment, Purchased_course

from django.db.models import Sum

from helpers.utils import get_timer

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
              
        count_ranking = Course_completion.objects.filter(completed_course__course_id=representation['id']).count()
        sum_ranking = Course_completion.objects.filter(completed_course__course_id=representation['id']).aggregate(Sum('rate_number'))['rate_number__sum']
        
        if sum_ranking==None:
            sum_ranking=0
 
        try:
            ranking = sum_ranking/count_ranking
        except ZeroDivisionError:
            ranking=0
        
        ranking = round(ranking, 1)
        
        representation['ranking']=ranking
        
        return representation
    

class EpisodeSerializer(ModelSerializer):
    section_id = serializers.StringRelatedField()
    video_length_time = serializers.SerializerMethodField()

    class Meta:
        model = Episode
        fields = ('title', 'file', 'place_number', 'length', 'section_id', 'video_length_time')

    def get_video_length_time(self, obj):
        return get_timer(obj.length)


class SectionSerializer(ModelSerializer):
    course_id = serializers.StringRelatedField()
    section_length_time = serializers.CharField(read_only=True)
    episodes = serializers.DictField(read_only=True) 
    
    class Meta:
        model = Section
        fields = ('section_title', 'section_number', 'section_type', 'is_public', 'course_id', 'section_length_time', 'episodes')


    def to_representation(self, instance):
        representation = super().to_representation(instance) 

        total_length = Episode.objects.filter(section_id=instance).aggregate(Sum('length'))['length__sum']
        
        if total_length==None:
            total_length=0 

        section_length_time = get_timer(total_length)
 
        episodes = Episode.objects.filter(section_id=instance)

 
        if episodes.exists():
            serializer = EpisodeSerializer(episodes, many=True)
            representation['episodes']= serializer.data 

        representation['section_length_time']=section_length_time
  
        return representation
     

class CourseRetrieveSerializer(ModelSerializer):
    category_id = serializers.StringRelatedField()
    sections = serializers.DictField(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'category_id', 'desciption', 'slider', 'author', 'sections')

        
    def to_representation(self, instance):
        representation = super().to_representation(instance) 

        sections = Section.objects.filter(course_id=instance)

 
        if sections.exists():
            serializer = SectionSerializer(sections, many=True)
            representation['sections'] = serializer.data  

        return representation