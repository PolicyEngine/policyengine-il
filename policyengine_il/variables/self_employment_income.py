from policyengine_il.model_api import *


class self_employment_income(Variable):
    label = "self-employment income"
    documentation = "Total self-employment income."
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"
