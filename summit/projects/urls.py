from django.conf.urls import url, include
from projects import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.project_index, name="project_index"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
