from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.models import Article


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


def article_detail(request):
    try:
        article = Article.objects.get(id=request.GET.get("id"))
    except Article.DoesNotExist:
        return HttpResponseRedirect("/")
    return render(request, "article_detail.html", context={"article": article})
