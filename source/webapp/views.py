from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.artcile_db import ArticleDb


# Create your views here.


def index(request):
    print(request.GET.getlist("my_params"))
    context = {
        "name": "john",
        "age": 20,
        "articles": ArticleDb.articles,
        "image_url": ArticleDb.image_url
    }
    return render(request, "index.html", context=context)


def create_article(request):
    if request.method == "GET":
        return render(request, "create_article.html")
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.POST.get("author")
        ArticleDb.articles.append(
            {
                "title": title,
                "content": content,
                "author": author
            }
        )
        return HttpResponseRedirect("/")
        # return render(request, "article.html", context={
        #     "title": title,
        #     "content": content,
        #     "author": author
        # })
