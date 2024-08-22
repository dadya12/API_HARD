import json
from datetime import datetime
from decimal import Decimal
from json import JSONDecodeError

from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.generics import get_object_or_404

from api_v2.serializers import ArticleSerializer
from webapp.models import Article


# Create your views here.
@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == 'GET':
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(permitted_methods=["GET"])


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by('-created_at')
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        serializer = ArticleSerializer(data=body)
        if serializer.is_valid():
            article = serializer.save()
            return JsonResponse({"pk": article.pk}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        body = json.loads(request.body)
        serializer = ArticleSerializer(data=body, instance=article)
        if serializer.is_valid():
            article = serializer.save()
            article_data = ArticleSerializer(article).data
            return JsonResponse(article_data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
