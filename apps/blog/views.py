from rest_framework import filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (
    CategoryBlogSerializer, BlogListSerializer,
    BlogDetailSerializer
)

from .models import Category_for_blog, Blog, Views

from rest_framework.permissions import AllowAny

from helpers.utils import get_client_ip

class CategoryBlogListAPIView(ListAPIView):
    queryset = Category_for_blog.objects.all()
    serializer_class = CategoryBlogSerializer
    permission_classes = (AllowAny,)
    pagination_class = (PageNumberPagination,)
    

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('title',) 
    filterset_fields = ('category_id',)
    permission_classes = (AllowAny,)
    pagination_class = (PageNumberPagination,)

class BlogRetrieveAPIView(RetrieveAPIView):
    serializer_class = BlogDetailSerializer
    queryset = Blog.objects.all()
    lookup_field = 'slug'
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
         
        if self.request.user.is_authenticated:
             
            Views.objects.update_or_create(
                blog_id=instance,
                user_id=self.request.user,
            )
        elif self.request.headers.get("device-id", None):
             
            Views.objects.update_or_create(
                blog_id=instance,
                device_id=self.request.headers.get("device-id", None),
            )
        else:
            ip = get_client_ip(self.request)

            Views.objects.update_or_create(
                blog_id=instance,
                ip_address=ip
            )

        return Response(serializer.data)
   
