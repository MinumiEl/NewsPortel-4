from django.urls import path

from . import views
from .views import PostList, PostsDetail, Search, ArticleUpdate, ArticleDelete, NewsUpdate, NewsDelete

urlpatterns = [
   path('', PostList.as_view()),
   path('news/', PostList.as_view()),
   path('post/<int:pk>/', PostsDetail.as_view()),
   path('news/search/', Search.as_view(), name='search'),
   path('news/create/', views.NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('articles/create/', views.ArticleCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),

]