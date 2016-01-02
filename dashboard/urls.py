from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'posts$', views.posts, name='posts'),
    url(r'posts/post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
    url(r'logout$', views.logout_user, name='logout_user'),
    url(r'login$', views.login_user, name="login_user"),
]
