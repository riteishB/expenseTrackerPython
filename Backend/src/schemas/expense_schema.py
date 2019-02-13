from schema import Schema, And, Use, Optional
import datetime


schema = Schema({
    'expense_name': And(str, len),
    'expense_amt': And(Use(float)),
    'expense_type': And(str, len),
    Optional('creation_date'): And(datetime.datetime),
    Optional('modified_date'): And(datetime.datetime)
})
