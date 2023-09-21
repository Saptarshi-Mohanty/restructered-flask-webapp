from pymongo.mongo_client import MongoClient

MONGO_URI = "mongodb+srv://smohanty:Xmq4m8BJOXJQdvn6@cluster0.ky6fr9w.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
stat = client.Employee.Stats