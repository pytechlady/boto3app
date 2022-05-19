from pymongo import MongoClient


connection_string = 'mongodb+srv://adebimpe_access:evhvZ68f40zeAzT6@prime.klo1e.mongodb.net/NG-STABLE?retryWrites=true&w=majority'
client = MongoClient('connection_string')
db = client['NG-STABLE']
print(db)
collection_name = db["MERCHANTS"]

profile_image = collection_name.find({})
for x in profile_image:
    print(x['profile_photo'])