from django.urls import path

from .views import CategoryListAPIView, CourseListAPIView

urlpatterns = [ 
    path('category/list/', CategoryListAPIView.as_view()),
    path('list/', CourseListAPIView.as_view())
]