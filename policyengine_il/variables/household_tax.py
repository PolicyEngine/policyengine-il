from policyengine_il.model_api import *


class household_tax(Variable):
    label = "tax"
    entity = Household
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"
