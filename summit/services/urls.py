from django.conf.urls import url, include
from services import views

urlpatterns = [
    url(r'^$', views.services_index, name="services_index"),
        url(r'^(?P<service_id>\d+)/(?P<slug>[\w-]+)$', views.service_detail,
        name="service_detail"),

]
