from app import Applicazione
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://grassigiovanni:giogalvani@cluster0.8hojujv.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))



def read_records (client):

    mydb = client["TopUni"]
    mycol = mydb["uniList"]

    for x in mycol.find():
        print(x)

read_records(client)