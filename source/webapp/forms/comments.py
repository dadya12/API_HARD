from django import forms
from django.forms import widgets

from webapp.models import Comment


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.visible_fields():
            v.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Comment
        fields = ("text", "author",)
