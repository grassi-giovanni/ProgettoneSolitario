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

@app.route('/ottieni_All')
def ottieni_All():
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


@app.route('/inserisci')
def inserisci():
    uri = "mongodb+srv://grassigiovanni:giogalvani@cluster0.8hojujv.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
   
    mydb = client["TopUni"]
    mycol = mydb["uniList"]


    data=( {
        "sequence": 2,
        "rank": 3,
        "university": "Milano",
        "overall_score": 98.9,
        "academic_reputation": 100,
        "employer_reputation": 100,
        "faculty_student_ratio": 100,
        "citations_per_faculty": 90.6,
        "international_faculty_ratio": 98.2,
        "international_students_ratio": 98.2,
        "international_research_network": 100,
        "employment_outcomes": 100,
        "sustainability": 97.8,
        "Fundos (US$)": 6.7
    })


    result = mycol.insert_one(data)
 
    return  {"status": "success", "data": "Inserita correttamente", "message": "dati insrit"}



if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

