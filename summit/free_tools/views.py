from django.shortcuts import render
from . import forms
import requests
from bs4 import BeautifulSoup
from free_tools.check import Check

# Create your views here.

def seoTool(request):
    form = forms.SeoToolForm()

    if request.method == 'POST':
        form = forms.SeoToolForm(request.POST)

        if form.is_valid():
            new_check = Check(form.cleaned_data['url'], form.cleaned_data['keyword'], form.cleaned_data['location'], [], [])
            new_check_soup = new_check.make_initial_request()
            print(new_check_soup)
            if new_check_soup == '':
                url_error = ["Sorry, We Couldn't Find Your URL. Try Again With a Valid URL."]
                form = forms.SeoToolForm()
                return render(request, 'free_tools/seo_tool.html', {'form': form, 'errors_list': url_error})

            new_check.check_title(new_check_soup)
            new_check.check_meta(new_check_soup)
            new_check.check_h1(new_check_soup)
            new_check.check_headers(new_check_soup)
            new_check.check_imgs(new_check_soup)
            new_check.content_checks(new_check_soup)

            print(new_check.kw_density)

            return render(request, 'free_tools/results.html', {'errors_list': new_check.page_errors,
                                                                'passing_list': new_check.page_passing,
                                                                'errors_count': new_check.errors_count,
                                                                'passing_count': new_check.passing_count,
                                                                'kw_density': new_check.kw_density,
                                                                'location_density' : new_check.loc_density})

    return render(request, 'free_tools/seo_tool.html', {'form': form})
