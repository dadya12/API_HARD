from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.artcile_db import ArticleDb
from webapp.models import Article


# Create your views here.


def index(request):
    articles = Article.objects.order_by("-created_at")
    return render(request, "index.html", context={"articles": articles})


def create_article(request):
    if request.method == "GET":
        return render(request, "create_article.html")
    else:
        Article.objects.create(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            author=request.POST.get("author")
        )
        return HttpResponseRedirect("/")
        # return render(request, "article.html", context={
        #     "title": title,
        #     "content": content,
        #     "author": author
        # })
