from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ArticleForm
from webapp.models import Article
from webapp.validate import article_validate


def index(request):
    articles = Article.objects.order_by("-created_at")
    return render(request, "index.html", context={"articles": articles})


def create_article(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, "create_article.html", {"form": form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data["content"],
                author=form.cleaned_data["author"]
            )
            return redirect("article_detail", pk=article.pk)

        return render(
            request,
            "create_article.html",
            {"form": form}
        )


def article_detail(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article_detail.html", context={"article": article})


def update_article(request, *args, pk, **kwargs):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=pk)
        form = ArticleForm(initial={
            "title": article.title,
            "author": article.author,
            "content": article.content,
        })
        return render(
            request, "update_article.html",
            context={"form": form}
        )
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = get_object_or_404(Article, pk=pk)
            article.title = form.cleaned_data['title']
            article.content = form.cleaned_data['content']
            article.author = form.cleaned_data['author']
            article.save()
            return redirect("article_detail", pk=article.pk)
        else:
            return render(
                request,
                "update_article.html",
                {"form": form}
            )


def delete_article(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, "delete_article.html", context={"article": article})
    else:
        article.delete()
        return redirect("articles")
