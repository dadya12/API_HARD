from django.urls import path

from webapp.views import index, create_article, article_detail

urlpatterns = [
    path('', index),
    path('create/', create_article),
]
