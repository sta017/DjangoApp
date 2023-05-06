from django.shortcuts import render

from rest_framework import viewsets
from .serializers import HeroInsuranceSerializer
from .models import HeroInsurance

# Create your views here.

class HeroInsuranceViewSet(viewsets.ModelViewSet):
	queryset = HeroInsurance.objects.all().order_by('name')
	serializer_class = HeroInsuranceSerializer
