from django.urls import path
from .views import (
    NewsList, News, PostCreate, PostUpdate, PostDelete,
    subscriptions,
)

from django.views.decorators.cache import cache_page


urlpatterns = [
    path('news/', cache_page(60)(NewsList.as_view())),
    path('<int:pk>', cache_page(300)(News.as_view()), name = 'post_detail'),
    path('news/create/', cache_page(300)(PostCreate.as_view()), name='news_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]