from django.urls import path

from .views import (
    CategoryBlogListAPIView, BlogListAPIView
)

urlpatterns = [
    path('category/list/', CategoryBlogListAPIView.as_view()),
    path('list/', BlogListAPIView.as_view()),
]