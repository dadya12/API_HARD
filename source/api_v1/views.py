import json
from datetime import datetime
from decimal import Decimal
from json import JSONDecodeError

from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from webapp.models import Article


# Create your views here.
@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == 'GET':
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(permitted_methods=["GET"])


def echo(request):
    if request.method == 'GET':
        my_dict = {
            "title": "test",
            "price": Decimal("100.00"),
            "created_at": datetime.now(),
        }
        # my_list = json.dumps(my_list)
        response = JsonResponse(my_dict)
        # response["Content-Type"] = "application/json"
    elif request.method == 'POST':
        try:
            title = json.loads(request.body).get("title", None)
            if title:
                response = JsonResponse(title, safe=False)
            else:
                response = HttpResponseBadRequest()
        except JSONDecodeError:
            response = HttpResponseBadRequest()
    else:
        response = HttpResponseNotAllowed(permitted_methods=["GET", "POST"])

    return response


def articles(request):
    if request.method == 'GET':
        articles = Article.objects.order_by('-created_at')
        articles_data = []

        for article in articles:
            articles_data.append(
                {
                    "title": article.title,
                    "content": article.content,
                    "status": article.status,
                }
            )

        return JsonResponse(articles_data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        print(request.user)
        Article.objects.create(**body, author=request.user)
        return HttpResponse(status=201)
    else:
        return HttpResponseNotAllowed(permitted_methods=["GET", "POST"])

