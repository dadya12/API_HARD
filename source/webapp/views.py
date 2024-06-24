from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse

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
        # return HttpResponseRedirect(reverse("articles"))
        # return HttpResponseRedirect(
        #     reverse("article_detail", kwargs={"pk": article.pk})
        # )
        return redirect("article_detail", pk=article.pk)


def article_detail(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    # try:
    #     article = Article.objects.get(id=pk)
    # except Article.DoesNotExist:
    #     raise Http404
    return render(request, "article_detail.html", context={"article": article})
