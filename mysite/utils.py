##link reference
## https://medium.com/featurepreneur/how-to-connect-a-django-project-with-mongodb-99f556cbb5b7
from pymongo import MongoClient

def get_db_handle(db_name=Insurance, host=localhost, port=27107, username=suraj, password=password):
  client = MongoClient(host=host,
			port=int(port),
			username=username,
			password=password)
  db_handle= client['db_name']
  
  return db_handle, client

def get_collection_handle(db_handle, collection_name=Providers):
  return db_handle[collection_name]
