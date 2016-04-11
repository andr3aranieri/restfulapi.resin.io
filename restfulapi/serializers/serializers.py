# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:30:16 2016

@author: isis
"""
from rest_framework import serializers
from restfulapi.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = {'id', 'firstname', 'lastname', 'studentid', 'tel', 'email', 'github', 'web'}        
