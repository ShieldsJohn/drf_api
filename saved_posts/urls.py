from django.urls import path
from .views import SavedPostList, SavedPostDetail


urlpatterns = [
    path('saved_posts/', SavedPostList.as_view()),
    path('saved_posts/<int:pk>/', SavedPostDetail.as_view()),
]
