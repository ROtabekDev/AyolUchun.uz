from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
)
from rest_framework.response import Response

from .models import Category_for_course, Course, Course_completion, Video_comment, Section, Episode

from .serializers import (
    CategoryForCourseListSerializer,
    CourseListSerializer,
    CourseRetrieveSerializer,
    PurchasedCourseSerializer,
    CompletedCourseSerializer,
    CourseCompletionSerializer,
    VideoCommentSerializar
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