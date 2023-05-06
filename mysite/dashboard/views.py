from django.shortcuts import render
from django.http import HttpResponse, request
from pymongo import MongoClient

#Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['Insurance']


# Insert the data into appropriate collection
def insert_data(data):
    try:
        # Use the upsert option to update the data if it already exists
        db['Providers'].insert_one(data, upsert=True)
    except Exception as e:
        # Log the error or return a failure response
        print(e)

# Handle an HTTP Post request
def handleSubmit(request):
    # Get the data from the request
    data = request.form.to_dict()

    # Validate the input
    if not data.get("name") or not data.get("value"):
        return "Error: Missing required fields"

    # Check the data types
    if not isinstance(data.get("value"), (int, float)):
        try:
            data["value"] = int(data["value"])
        except ValueError:
            try:
                data["value"] = float(data["value"])
            except ValueError:
                return "Error: Invalid value"

    # Insert the data into the database
    insert_data(data)

    # Return a success response
    return "Success!"

#Serve the HTML file
#@app.route('/')
def operation(request):
	return render(request, 'Insurance_compare.html')
