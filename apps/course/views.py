from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Category_for_course, Course, Section, Episode

from .serializers import (
    CategoryForCourseListSerializer,
    CourseListSerializer,
    CourseRetrieveSerializer
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