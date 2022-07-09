from django import forms
from .models import ShortUrl


class ShorturlForm(forms.ModelForm):

    long_url = forms.URLField(widget=forms.URLInput(
        attrs=
        {
            "class": "url-form",
            "placeholder": "Введите URL"
        }
    ))

    class Meta:
        model = ShortUrl

        fields = ('long_url',)
