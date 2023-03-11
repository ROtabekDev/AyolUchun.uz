from rest_framework.generics import ListAPIView, RetrieveAPIView

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

class BlogRetrieveAPIView(RetrieveAPIView):
    serializer_class = BlogDetailSerializer
    queryset = Blog.objects.all()
    lookup_field = 'slug'

