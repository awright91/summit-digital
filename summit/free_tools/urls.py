from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^small-business-seo-tool/$', views.seoTool, name="seo_tool"),
]
