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
        collection = db['Providers']

        # Insert the form data into the MongoDB collection
        name = request.POST.get('name')
        value = request.POST.get('value')
        collection.insert_one({'name': name, 'value': value})

        return HttpResponse("Form submission successful!")
    else:
        return render(request, 'form.html')

def display(request):
    # Connect to the MongoDB Database
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['Insurance']
    collection = db['Providers']

    #Retrieving the data from the collection
#    print(Data.objects.all().query)              #added for troubleshoot
    cursor = collection.find()
    data_list =list(cursor)
#    print(data_list)                             #added for Troubleshoot
    context = {'data_list': data_list}
    return render(request, 'display.html', context)



#class DataViewSet(viewsets.ModelViewSet):
#    queryset = Data.objects.all()
#    serializer_class = DataSerializer
