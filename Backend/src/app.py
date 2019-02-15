from flask import Flask
from flask import request
import random as rand
import string
import datetime
from flask import jsonify
import json

from libs import mongo_client
from schemas import expense_schema

app = Flask(__name__)

collection = mongo_client.getCollection()


#@app.route('/')  # GET route
# def hello_world():
#     return 'Hello world'

@app.route('/')
def get_expenses():
    expenses = []
    for expense in collection.find():
        del expense['_id']

        expenses.append(expense)

    return jsonify(expenses)



@app.route('/<expense_id>')
def getHandler(expense_id):

    expense = collection.find_one({"id": expense_id})

    if (expense == None):
        return 'Not found', 404

    del expense['_id']
    return jsonify(expense)


@app.route('/', methods=['POST'])
def postHandler():
    content = request.get_json()
    expense_schema.schema.validate(content)

    # if data is valid data
    if(validateExpenseData(content)):
        # generate id
        id = generateID()

        # check if id is already in use or not
        data = collection.find({"id": id})

        # Until an unique id is found, keep creating new id
        # data.count returns count for data -- built in syntax for count
        while(data.count() > 0):
            id = generateID()
            data = collection.find({'id': id})

        #  update the json data to contain the id
        content['id'] = id
        #  update the json data to have a creation date for the initial creation
        content['creation_date'] = datetime.datetime.now()

        # once we have the data in the form we need it, we insert it to the db collection
        collection.insert_one(content)

        return id, 201
    else:
        return 'Invalid Data', 400


@app.route('/<expense_id>', methods=['PUT'])  
def putHandler(expense_id):
    #  get the data from the body and  validate the schema
    content = request.get_json()
    
    #  if the document in the body is valid
    if(validateExpenseData(content)):
        content['modified_date'] = datetime.datetime.now()
        response = collection.update_one({"id": expense_id}, { "$set": content })
        if(response.modified_count == 0):
            return 'Expense not found', 400
            
        return 'OK', 200
    else:
        return 'Invalid Data', 400

def generateID():
    return ''.join(rand.choice(string.ascii_uppercase + string.digits) for _ in range(6))


def validateExpenseData(data):
    isValid = expense_schema.schema.is_valid(data)
    return isValid
