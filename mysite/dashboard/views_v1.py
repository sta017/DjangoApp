from django.shortcuts import render
from django.http import HttpResponse, request

def operation(request):
	return render(request, 'Insurance_compare.html')
