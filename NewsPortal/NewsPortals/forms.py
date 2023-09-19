from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    heading = forms.CharField(min_length=20)
    class Meta:
        model = Post
        fields = ['author', 'category', 'heading', 'text', 'rating']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")

        if text is None:
            raise ValidationError(
                "Напишите текст"
            )