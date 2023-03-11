from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (
    CategoryBlogSerializer, BlogListSerializer,
    BlogDetailSerializer
)

from .models import Category_for_blog, Blog

class CategoryBlogListAPIView(ListAPIView):
    queryset = Category_for_blog.objects.all()
    serializer_class = CategoryBlogSerializer

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('title',) 
    filterset_fields = ('category_id',)

class BlogRetrieveAPIView(RetrieveAPIView):
    serializer_class = BlogDetailSerializer
    queryset = Blog.objects.all()
    lookup_field = 'slug'

