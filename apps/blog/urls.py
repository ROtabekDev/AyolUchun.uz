from django.urls import path

from .views import (
    CategoryBlogListAPIView, BlogListAPIView, BlogRetrieveAPIView
)

urlpatterns = [
    path('category/list/', CategoryBlogListAPIView.as_view()),
    path('list/', BlogListAPIView.as_view()),
    path('detail/<str:slug>/', BlogRetrieveAPIView.as_view()),
]