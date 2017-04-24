from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    telephone = forms.CharField()
    message = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])


    name.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telephone.widget.attrs['class'] = 'form-control'
    message.widget.attrs['class'] = 'form-control'
