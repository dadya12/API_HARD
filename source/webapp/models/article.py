from django.db import models

from webapp.models import BaseModel

statuses = [("new", "Новая"), ("moderated", "Модерированная"), ("deleted", "Удаленная")]


class Article(BaseModel):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="Автор", default="Неизвестный")
    content = models.TextField(null=False, blank=False, verbose_name="Контент")
    status = models.CharField(max_length=20, choices=statuses, verbose_name="Статус", default=statuses[0][0])
    # tags = models.ManyToManyField("webapp.Tag", related_name="articles", verbose_name="Теги", blank=True)
    tags = models.ManyToManyField(
        "webapp.Tag",
        related_name="articles",
        verbose_name="Теги",
        blank=True,
        through='webapp.ArticleTag',
        through_fields=("article", "tag"),
    )

    def __str__(self):
        return f"{self.pk}. {self.title}: {self.author}"

    class Meta:
        db_table = "articles"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
