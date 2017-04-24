from django import forms
from django.core import validators


class SeoToolForm(forms.Form):
    url = forms.URLField()
    keyword = forms.CharField()
    location = forms.CharField()

    url.widget.attrs['class'] = 'form-control'
    keyword.widget.attrs['class'] = 'form-control'
    location.widget.attrs['class'] = 'form-control'
