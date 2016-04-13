# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:01:31 2016

@author: andrea.ranieri@protonmail.com
"""

from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^students/$', views.StudentsList.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
