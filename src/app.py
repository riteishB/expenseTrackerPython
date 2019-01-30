from flask import Flask
from flask import request
import random as rand
import string
import datetime
#import pymongo
from pymongo import MongoClient
import config
from schemas import expense_schema

app = Flask(__name__)

client = MongoClient()

uri = "mongodb://"+config.MONGO_USER+":"+config.MONGO_PASSWORD+"@ds115022.mlab.com:15022/expense-tracker"
client = MongoClient(uri)
db = client.get_default_database()

@app.route('/')  # GET route
def hello_world():
    print(db)
    return 'Hello world'


@app.route('/', methods=['POST'])
def postHandler():

    content = request.get_json()
    #content["creation_date"] = datetime.datetime.now()
    #content["modified_date"] = datetime.datetime.now()
    expense_schema.schema.validate(content)
    
    if(validateExpenseData(content)):
        id = generateID()
        return id, 200
    else:
        return 'Invalid Data', 400


def generateID():
    return ''.join(rand.choice(string.ascii_uppercase + string.digits) for _ in range(6))


def validateExpenseData(data):
    isValid = expense_schema.schema.is_valid(data)
    return isValid
