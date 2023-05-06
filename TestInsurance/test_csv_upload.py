import csv
from pymongo import MongoClient

#Connect to database
client = MongoClient("mongodb://localhost:27017/")
db = client["Insurance"]
collection = db["Providers"]
filename = "test_insur_data.csv"

#Open csv file and read the rows
with open(filename, "r") as csv_file:
   reader = csv.DictReader(csv_file)

   #Iterate through the rows and insert each to collection
   for row in reader:
       collection.insert_one(row)

