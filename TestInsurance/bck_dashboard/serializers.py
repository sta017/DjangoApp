
from rest_framework import serializers
from .models import HeroInsurance

class HeroInsuranceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
     model = HeroInsurance
     fields = ('name', 'value')


