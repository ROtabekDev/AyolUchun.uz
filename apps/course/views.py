from rest_framework.generics import ListAPIView

from .models import Category_for_course

from .serializers import (
    CategoryForCourseListSerializer,
)


class CategoryListAPIView(ListAPIView):
    queryset = Category_for_course.objects.all()
    serializer_class = CategoryForCourseListSerializer