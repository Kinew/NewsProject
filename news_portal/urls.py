from django.urls import path
from .views import (NewsList, News, PostCreate, PostUpdate, PostDelete)

urlpatterns = [
    path('news/', NewsList.as_view()),
    path('<int:pk>', News.as_view(), name = 'post_detail'),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]