from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Tag, Article


def title_validate(title):
    if len(title) < 5:
        raise ValidationError("error")


class ArticleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.visible_fields():
            v.field.widget.attrs["class"] = "form-control"

    title = forms.CharField(max_length=50, required=True, label="Название", validators=[title_validate])
    author = forms.CharField(
        max_length=50,
        required=False,
        label="Автор",
        initial="Неизвестный",
        widget=widgets.Input(attrs={"placeholder": "Автор"}),
    )
    content = forms.CharField(
        max_length=3000,
        required=True,
        label="Контент",
        widget=widgets.Textarea(attrs={"cols": 20, "rows": 5, "placeholder": "Контент"}),
    )
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=True)

    # def clean_title(self):
    #     title = self.cleaned_data["title"]
    #     if len(title) < 5:
    #         raise ValidationError("error")
    #     return title

    def clean(self):
        title = self.cleaned_data.get("title")
        content = self.cleaned_data.get("content")
        if title and content and title == content:
            raise ValidationError("clean - error")
        return super().clean()
