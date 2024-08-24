from django.urls import path

from api_v2.views.articles import get_csrf_token, ArticleView
from api_v2.views.comments import CommentAPIView

app_name = 'api_v2'

urlpatterns = [
    path('get-token/', get_csrf_token, name='get_token'),
    path('articles/', ArticleView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleView.as_view(), name='article'),
    path('articles/<int:pk>/comments/', CommentAPIView.as_view(), name='comments'),
    path('articles/comments/<int:comment_pk>/', CommentAPIView.as_view(), name='comment-detail'),
]
