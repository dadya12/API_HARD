from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from api_v2.serializers import CommentSerializer
from webapp.models import Article, Comment


class CommentAPIView(APIView):
    def get(self, request, *args, pk=None, comment_id=None, **kwargs):
        if pk:
            comments = Comment.objects.order_by('-created_at').filter(article_id=pk)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif comment_id:
            comment = get_object_or_404(Comment, pk=comment_id)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
