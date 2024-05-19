# import os
# from dotenv import load_dotenv
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

# db_password = os.getenv("DB_PASSWORD")

# uri = "mongodb+srv://alokshandilya:{db_password}@cluster0.snyhuvn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri = "mongodb+srv://alokshandilya:V9Ow23uoUwD41rca@cluster0.snyhuvn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
