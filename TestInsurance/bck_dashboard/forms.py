
from django import forms

class HeroInsuranceForm(forms.Form):
    name = forms.CharField(max_length=100)
    value = forms.CharField(max_length=100)
