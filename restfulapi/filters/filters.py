# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 14:51:18 2016

@author: andrea.ranieri@protonmail.com
"""

import django_filters
from rest_framework import filters
from rest_framework import generics

from restfulapi.models import Student

class StudentFilter(filters.FilterSet):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname']
