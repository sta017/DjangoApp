
from django import forms

class InformationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    value = forms.CharField(label='Value', max_length=100)
