from django.urls import path
from django.views.generic import RedirectView

from webapp.views import update_article, delete_article, ArticleListView, CreateArticleView, \
    ArticleDetailView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('', RedirectView.as_view(pattern_name='articles')),
    path('create/', CreateArticleView.as_view(), name='create_article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/update/', update_article, name='update_article'),
    path('article/<int:pk>/delete/', delete_article, name='delete_article'),
]
