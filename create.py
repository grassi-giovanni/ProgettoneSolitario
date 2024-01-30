from app import Applicazione
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


#Operazioni CRUD

# CREATE
def create_record(data):
    uri = "mongodb+srv://grassigiovanni:giogalvani@cluster0.8hojujv.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    mydb = client["TopUni"]
    mycol = mydb["uniList"]
    result = mycol.insert_one(data)
    print(f"Record creato con ID: {result.inserted_id}")


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

create_record(data)

