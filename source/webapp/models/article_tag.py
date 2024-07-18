from django.db import models

from webapp.models import BaseModel


class ArticleTag(BaseModel):
    article = models.ForeignKey('webapp.Article', related_name='tags_articles', on_delete=models.CASCADE, )
    tag = models.ForeignKey('webapp.Tag', related_name='articles_tags', on_delete=models.CASCADE, )
