from flask import Flask
from flask import request
import random as rand
import string
import datetime

from libs import mongo_client
from schemas import expense_schema

app = Flask(__name__)

collection = mongo_client.getCollection()


@app.route('/')  # GET route
def hello_world():
    return 'Hello world'


@app.route('/', methods=['POST'])
def postHandler():
    content = request.get_json()
    expense_schema.schema.validate(content)

    # if data is valid data
    if(validateExpenseData(content)):
        # generate id
        id = generateID()
        #  update the json data to contain the id
        content['id'] = id
        #  update the json data to have a creation date for the initial creation
        content['creation_date'] = datetime.datetime.now()

        # once we have the data in the form we need it, we insert it to the db collection
        collection.insert_one(content)

        return id, 201
    else:
        return 'Invalid Data', 400


def generateID():
    return ''.join(rand.choice(string.ascii_uppercase + string.digits) for _ in range(6))


def validateExpenseData(data):
    isValid = expense_schema.schema.is_valid(data)
    return isValid
