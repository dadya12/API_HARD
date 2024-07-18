from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import CommentForm
from webapp.models import Article


class CreateCommentView(CreateView):
    template_name = "comments/create_comment.html"
    form_class = CommentForm

    # def form_valid(self, form):
    #     article = get_object_or_404(Article, pk=self.kwargs['pk'])
    #     form.instance.article = article
    #     return super().form_valid(form)

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(article.get_absolute_url())

    # def get_success_url(self):
    #     return reverse("article_detail", kwargs={"pk": self.object.article.pk})
