from django.urls import path
from .views import PostList, PostsDetail


urlpatterns = [
   path('news/', PostList.as_view()),
   path('post/<int:pk>/', PostsDetail.as_view()),
]