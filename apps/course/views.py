from rest_framework.generics import ListAPIView

from .models import Category_for_course, Course, Section, Episode

from .serializers import (
    CategoryForCourseListSerializer,
    CourseListSerializer
)


class CategoryListAPIView(ListAPIView):
    queryset = Category_for_course.objects.all()
    serializer_class = CategoryForCourseListSerializer


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer