# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import Index


urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^about/', TemplateView.as_view(template_name="about.html"),
        name="about"),
)