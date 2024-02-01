import os 
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
CORS(app)

class Applicazione  :
    #SI CONNETTE A IL SERVER E LO PINGA
    #conferma con daje roma
    uri = "mongodb+srv://grassigiovanni:giogalvani@cluster0.8hojujv.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("DAJJJJEE ROMA DAJJEEEEE")
    except Exception as e:
       print(e)

    database_name = 'TopUni'
    db = client[database_name]

    # Esegui una query o altre operazioni specifiche per il database 'TopUni'
    # Ad esempio, puoi ottenere la lista delle collezioni nel database 'TopUni'
    collection_names = db.list_collection_names()
    print(f"Collezioni nel database '{database_name}': {collection_names}")

@app.route('/simple_json')
def simple_json():
    uri = "mongodb+srv://grassigiovanni:giogalvani@cluster0.8hojujv.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
   
    mydb = client["TopUni"]
    mycol = mydb["uniList"]


    output = []
    for x in mycol.find({},{'_id': 0}):
        output.append(x)

    print (output)

    return jsonify({'DATI OTTENUTI': output})


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

