from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import generics
from rest_framework import filters

from .serializers.serializers import StudentSerializer
from .models import Student
from .filters.filters import StudentFilter

def index(request):
    return HttpResponse("Django RESTfulAPI deployed with resin.io. This will be shown after the end of the presentation.")

class StudentsList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
