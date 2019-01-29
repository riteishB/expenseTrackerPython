from schema import Schema, And, Use, Optional


schema = Schema({
    'name': And(str, len)})
