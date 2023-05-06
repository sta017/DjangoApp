
from rest_framework import serializers
from .models import BestInsurance

class BestInsuranceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
     model = BestInsurance
     fields = ('name', 'value')


