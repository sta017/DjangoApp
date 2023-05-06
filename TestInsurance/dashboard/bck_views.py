from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DataSerializer
from .models import Data
from django.http import HttpResponse
import pymongo

def submit(request):
    if request.method == 'POST':
        # Connect to the MongoDB database
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['Insurance']
	collection = db['test_collection']

        # Insert the form data into the MongoDB collection
        name = request.POST['name']
        value = request.POST['value']
        collection.insert_one({'name': name, 'value': value})

        return HttpResponse('Form submission successful!')
    else:
        return render(request, 'form.html')

def display(request):
    data_list = Data.objects.all()
    context = {'data_list': data_list}
    return render(request, 'display.html', context)



#class DataViewSet(viewsets.ModelViewSet):
#    queryset = Data.objects.all()
#    serializer_class = DataSerializer
