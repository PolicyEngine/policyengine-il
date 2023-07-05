from policyengine_il.model_api import *


class gross_income(Variable):
    label = "gross income"
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"
    adds = ["employment_income"]
