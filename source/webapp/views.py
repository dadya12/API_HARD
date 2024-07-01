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


def update_article(request, *args, pk, **kwargs):
    if request.method == "GET":
        return render(
            request, "update_article.html",
            context={"article": get_object_or_404(Article, pk=pk)}
        )
    else:
        article = get_object_or_404(Article, pk=pk)
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.author = request.POST.get("author")
        article.save()
        return redirect("article_detail", pk=article.pk)


def delete_article(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, "delete_article.html", context={"article": article})
    else:
        article.delete()
        return redirect("articles")
