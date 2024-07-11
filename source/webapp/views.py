from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import ArticleForm
from webapp.models import Article


class ArticleListView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by("-created_at")
        return render(request, "index.html", context={"articles": articles})


class CreateArticleView(View):
    def dispatch(self, request, *args, **kwargs):
        print(request.POST)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "create_article.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data["content"],
                author=form.cleaned_data["author"]
            )
            tags = form.cleaned_data["tags"]
            article.tags.set(tags)
            return redirect("article_detail", pk=article.pk)
        return render(
            request,
            "create_article.html",
            {"form": form}
        )


class ArticleDetailView(TemplateView):
    # template_name = "article_detail.html"

    def dispatch(self, request, *args, **kwargs):
        self.article = get_object_or_404(Article, pk=kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["article"] = self.article
        return context

    def get_template_names(self):
        if self.article.tags.exists():
            return ["article_detail.html"]
        else:
            return ["test_detail.html"]


def update_article(request, *args, pk, **kwargs):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=pk)
        form = ArticleForm(initial={
            "title": article.title,
            "author": article.author,
            "content": article.content,
            "tags": article.tags.all()
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
            tags = form.cleaned_data["tags"]
            article.tags.set(tags)
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
