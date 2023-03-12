from django.urls import path

from .views import CategoryListAPIView, CourseListAPIView, CourseRetrieveAPIView

urlpatterns = [ 
    path('category/list/', CategoryListAPIView.as_view()),
    path('list/', CourseListAPIView.as_view()),
    path('detail/<str:slug>/', CourseRetrieveAPIView.as_view())
]