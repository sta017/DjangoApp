from django.shortcuts import render

from rest_framework import viewsets
from .serializers import InsuranceSerializer
from .models import Insurance
 
# Create your views here.

class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all().order_by('name')
    serializer_class = InsuranceSerializer
