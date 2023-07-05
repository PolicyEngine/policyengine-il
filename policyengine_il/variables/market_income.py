from policyengine_il.model_api import *


class market_income(Variable):
    label = "market income"
    documentation = "Total non-government income."
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"
    adds = ["employment_income"]
