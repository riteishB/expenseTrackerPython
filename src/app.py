from flask import Flask
from flask import request
import random as rand
import string

app = Flask(__name__)

@app.route('/')  #GET route
def hello_world():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def postHandler():
    #content = request.get_json()
    id = generateID()
    return id

def generateID():
    return ''.join(rand.choice(string.ascii_uppercase + string.digits) for _ in range(6))




