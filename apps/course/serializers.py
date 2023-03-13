from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category_for_course, Course, Section, Episode, Course_completion, Video_comment, Purchased_course, Completed_course, Episode_viewed

from apps.user.serializers import UserSerializer

from django.db.models import Sum, Q

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
    comments = serializers.DictField(read_only=True) 
    class Meta:
        model = Episode
        fields = ('title', 'slug', 'file', 'place_number', 'length', 'section_id', 'video_length_time', 'comments')

    def get_video_length_time(self, obj):
        return get_timer(obj.length)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)  
 
        comments = Video_comment.objects.filter(episode_id=instance)

 
        if comments.exists():
            serializer = VideoCommentSerializar(comments, many=True)
            representation['comments']= serializer.data 
 
        return representation


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
        
        if sections.filter(~Q(section_type='Reviewed')).exists():
            print('bingo')
        else:
            Completed_course.objects.create(user_id=self.context['request'].user, course_id=instance) 

        return representation
    

class CourseUnPaidRetrieveSerializer(ModelSerializer):
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
    

class PurchasedCourseSerializer(ModelSerializer):

    class Meta:
        model = Purchased_course
        fields = ('user_id', 'course_id')


class CompletedCourseSerializer(ModelSerializer):

    class Meta:
        model = Completed_course
        fields = ('user_id', 'course_id')


class CourseCompletionSerializer(ModelSerializer):
    completed_course = CompletedCourseSerializer()

    class Meta:
        model = Course_completion
        fields = ('completed_course', 'rate_number', 'message')     


class VideoCommentSerializar(ModelSerializer):
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Video_comment
        fields = ('user', 'parent', 'episode_id', 'text', 'is_child')