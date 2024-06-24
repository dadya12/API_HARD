from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Article


def index(request):
    articles = Article.objects.order_by("-created_at")
    return render(request, "index.html", context={"articles": articles})


def create_article(request):
    if request.method == "GET":
        return render(request, "create_article.html")
    else:
        article = Article.objects.create(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            author=request.POST.get("author")
        )
        return redirect("article_detail", pk=article.pk)


def article_detail(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article_detail.html", context={"article": article})
