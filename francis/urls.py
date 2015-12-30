"""francis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from francis import settings
import blog
import dashboard

urlpatterns = [
    url(r'^', include('blog.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^dashboard/login$', dashboard.views.login_user, name="login_user"),
]

if settings.ADMIN_ENABLED:
    urlpatterns.append(url(r'^admin/', admin.site.urls))

# This needs to be added last!
urlpatterns.append(url(r'^(?P<page_slug>.+)/$', blog.views.slugged_page,
    name='slugged_page'))
