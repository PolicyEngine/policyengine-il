from policyengine_il.model_api import *


class pension_income(Variable):
    label = "pension income"
    documentation = "Total pension income."
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"
