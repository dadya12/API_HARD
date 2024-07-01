from django.urls import path

from webapp.views import index, create_article, article_detail, update_article, delete_article

urlpatterns = [
    path('', index, name='articles'),
    path('create/', create_article, name='create_article'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/<int:pk>/update/', update_article, name='update_article'),
    path('article/<int:pk>/delete/', delete_article, name='delete_article'),
]
