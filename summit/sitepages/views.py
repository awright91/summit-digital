from django.shortcuts import render
from services.models import Service
from projects.models import Project
from . import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    services = Service.objects.all
    return render(request, 'sitepages/home.html', {'services': services})


def contact(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])


    return render(request, 'sitepages/contact.html', {'form': form })
