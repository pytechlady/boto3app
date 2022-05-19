from pymongo import MongoClient
import os


connection_string = os.environ.get('MONGO_DB_CONNECTION_STRING')
client = MongoClient('connection_string')
db = client['NG-STABLE']
print(db)
collection_name = db["MERCHANTS"]

profile_image = collection_name.find({})
for x in profile_image:
    print(x)