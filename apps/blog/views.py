from rest_framework.generics import ListAPIView

from .serializers import (
    CategoryBlogSerializer, BlogListSerializer
)

from .models import Category_for_blog, Blog

class CategoryBlogListAPIView(ListAPIView):
    queryset = Category_for_blog.objects.all()
    serializer_class = CategoryBlogSerializer

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer

