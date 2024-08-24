from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from api_v2.serializers import CommentSerializer
from webapp.models import Article, Comment


class CommentAPIView(APIView):
    def get(self, request, *args, pk=None, comment_pk=None, **kwargs):
        if pk:
            comments = Comment.objects.order_by('-created_at').filter(article_id=pk)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif comment_pk:
            comment = get_object_or_404(Comment, pk=comment_pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, pk, **kwargs):
        request_data = request.data.copy()
        request_data['article'] = pk
        serializer = CommentSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        comment_data = CommentSerializer(comment).data
        return Response(comment_data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, comment_pk=None, **kwargs):
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment_pk:
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            comment_data = CommentSerializer(comment).data
            return Response(comment_data, status=status.HTTP_200_OK)
        else:
            serializer = CommentSerializer(comment, data=request.data)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, comment_pk=None, **kwargs):
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment_pk:
            comment.delete()
            return Response({'deleted_comment': comment_pk}, status=status.HTTP_204_NO_CONTENT)
