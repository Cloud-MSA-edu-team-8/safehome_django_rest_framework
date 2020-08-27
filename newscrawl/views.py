from django.shortcuts import render
from rest_framework import generics

from .models import NewsData
from .serializers import NewsSerializer

# news
class ListNews(generics.ListCreateAPIView):
    queryset = NewsData.objects.all()
    serializer_class = NewsSerializer

class DetailNews(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsData.objects.all()
    serializer_class = NewsSerializer