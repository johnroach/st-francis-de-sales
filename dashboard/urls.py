from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'posts$', views.posts, name='posts'),
    url(r'logout$', views.logout_user, name='logout_user'),
    url(r'login$', views.login_user, name="login_user"),
]
