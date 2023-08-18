from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'categoryType',
            'postCategory',
            'text',
        ]

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get("title")
            description = cleaned_data.get("text")

            if name == description:
                raise ValidationError(
                    "Описание не должно быть идентично названию."
                )

            return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'categoryType',
            'postCategory',
            'text',
        ]

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get("title")
            description = cleaned_data.get("text")

            if name == description:
                raise ValidationError(
                    "Описание не должно быть идентично названию."
                )

            return cleaned_data
