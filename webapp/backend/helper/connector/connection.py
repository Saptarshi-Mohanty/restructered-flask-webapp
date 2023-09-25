from pymongo.mongo_client import MongoClient
from backend.core.config import MONGO_URI

client = MongoClient(MONGO_URI)
stat = client.Employee.Stats