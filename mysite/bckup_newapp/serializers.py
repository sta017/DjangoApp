
from rest_framework import serializers
from .models import Insurance

class InsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model= Insurance
#       fields=('name', 'plan','benefits','payment','sum')
       fields = ('name', 'plan_type','death_benefits','payment_mode','sum_assured')

