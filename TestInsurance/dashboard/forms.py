
from django import forms

class InformationForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=100)
    Value = forms.CharField(label='Value', max_length=100)
