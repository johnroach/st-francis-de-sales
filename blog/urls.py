from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search_result, name="search_result"),
    url(r'^tag/(?P<tags>(?:\w+/)+)$', views.tagged_posts, name='tagged_posts'),
    url(r'^category/(?P<categories>(?:\w+/)+)$', views.categoried_posts, name='categoried_posts'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<url_slug>[-\w]*)/$', views.single_post, name='single_post'),
]
