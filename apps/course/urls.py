from django.urls import path

from .views import (
    CategoryListAPIView, CourseListAPIView, 
    CourseRetrieveAPIView, PurchasedCourseCreateAPIView,
    CompletedCourseCreateAPIView, CourseCompletionCreateListAPIView,
    CommentListCreateAPIView
)

urlpatterns = [ 
    path('category/list/', CategoryListAPIView.as_view()),
    path('list/', CourseListAPIView.as_view()),
    path('detail/<str:slug>/', CourseRetrieveAPIView.as_view()),

    path('create-purchased-course/', PurchasedCourseCreateAPIView.as_view()),
    path('create-completed-course/', CompletedCourseCreateAPIView.as_view()),
    path('create-list-course-completion/', CourseCompletionCreateListAPIView.as_view()),
    
    path('comment/list-create/', CommentListCreateAPIView.as_view()), 
]