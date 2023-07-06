from policyengine_il.model_api import *


class tax(Variable):
    label = "individual tax"
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"
    adds = [
        "municipal_tax",
    ]
