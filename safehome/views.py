from django.shortcuts import render

from django.shortcuts import render
from rest_framework import generics

from .models import Children, Crime, Fire_damage, Flood, Alchohol, House
from .serializers import CrimeSerializer


# crime
class ListCrime(generics.ListCreateAPIView):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer

class DetailCrime(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer

