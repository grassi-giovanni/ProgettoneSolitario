from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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


