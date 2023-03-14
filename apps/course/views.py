import os

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
)

from .models import Category_for_course, Course, Course_completion, Video_comment, Section, Episode, Episode_viewed

from .serializers import (
    CategoryForCourseListSerializer,
    CourseListSerializer,
    CourseRetrieveSerializer,
    PurchasedCourseSerializer,
    CompletedCourseSerializer,
    CourseCompletionSerializer,
    VideoCommentSerializar,
    CourseUnPaidRetrieveSerializer
)


class CategoryListAPIView(ListAPIView):
    queryset = Category_for_course.objects.all()
    serializer_class = CategoryForCourseListSerializer


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filterset_fields = ('category_id',) 


class CourseRetrieveAPIView(RetrieveAPIView):
    serializer_class = CourseRetrieveSerializer
    queryset = Course.objects.all()
    lookup_field = 'slug' 

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        sections = Section.objects.filter(course_id=instance)

        for section in sections:
            episodes = Episode.objects.filter(section_id=section)
            episode_viewed=0
            episodes_length = episodes.count()

            for episode in episodes:
                if Episode_viewed.objects.filter(episode_id=episode, user_id=request.user).exists():
                    episode_viewed +=1
            
            if episode_viewed == 0: 
                section.section_type = 'Not seen'
                section.save()
            elif episode_viewed < episodes_length:  
                section.section_type = 'In progress'
                section.save()
            else: 
                section.section_type = 'Reviewed'
                section.save()  
        
        serializer = self.get_serializer(instance)
        
        return Response(serializer.data)


class CourseUnPaidRetrieveAPIView(RetrieveAPIView):
    serializer_class = CourseUnPaidRetrieveSerializer
    queryset = Course.objects.all()
    lookup_field = 'slug' 

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        public_sections = Section.objects.filter(course_id=instance).filter(is_public=True)

        for section in public_sections:
            episodes = Episode.objects.filter(section_id=section)
            episode_viewed=0
            episodes_length = episodes.count()

            for episode in episodes:
                if Episode_viewed.objects.filter(episode_id=episode, user_id=request.user).exists():
                    episode_viewed +=1
            
            if episode_viewed == 0: 
                section.section_type = 'Not seen'
                section.save()
            elif episode_viewed < episodes_length:  
                section.section_type = 'In progress'
                section.save()
            else: 
                section.section_type = 'Reviewed'
                section.save()  
        
        private_sections = Section.objects.filter(course_id=instance).filter(is_public=False)

        for section in private_sections: 
            section.section_type = 'Not purchased'
            section.save()

        serializer = self.get_serializer(instance)
        
        return Response(serializer.data)

class PurchasedCourseCreateAPIView(CreateAPIView):
    serializer_class = PurchasedCourseSerializer


class CompletedCourseCreateAPIView(CreateAPIView):
    serializer_class = CompletedCourseSerializer


class CourseCompletionCreateListAPIView(ListCreateAPIView):
    queryset = Course_completion.objects.all()
    serializer_class = CourseCompletionSerializer


class CommentListCreateAPIView(ListCreateAPIView):  
    queryset = Video_comment.objects.all()
    serializer_class = VideoCommentSerializar
    filterset_fields = ('episode_id',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StreamingVideoView(APIView):

    def get(self, request, slug):
        self.episode = get_object_or_404(Episode, slug=slug)
        if os.path.exists(self.episode.file.path):
            response = HttpResponse('', content_type="video/mp4", status=206)
            response['X-Accel-Redirect'] = f"/mp4/{self.episode.file.name}"
                         
            Episode_viewed.objects.create(user_id=request.user, episode_id=self.episode)
                        
            return response
        else:
            return Http404