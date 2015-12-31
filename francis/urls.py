"""francis URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
"""
from django.conf.urls import include, url
from django.contrib import admin
from francis import settings
import blog
import dashboard

urlpatterns = [
    url(r'^dashboard', include('dashboard.urls')),
    url(r'^', include('blog.urls')),
]

if settings.ADMIN_ENABLED:
    urlpatterns.append(url(r'^admin/', admin.site.urls))

# This needs to be added last!
urlpatterns.append(url(r'^(?P<page_slug>.+)/$', blog.views.slugged_page,
    name='slugged_page'))
