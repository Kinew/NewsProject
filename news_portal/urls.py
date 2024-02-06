from django.urls import path
from .views import NewsList, News

urlpatterns = [
    path('news/', NewsList.as_view()),
    path('<int:pk>', News.as_view()),
    path('create/', NewsCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
]