from django.conf.urls import url, include
from posts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.blog_index, name="blog_index"),
    url(r'^(?P<post_id>\d+)/(?P<slug>[\w-]+)$', views.post_detail,
        name="post_detail"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
