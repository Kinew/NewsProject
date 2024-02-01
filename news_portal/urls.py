from django.urls import path
from .views import NewsList, News

urlpatterns = [
    path('news/', NewsList.as_view()),
    path('<int:pk>', News.as_view()),
]