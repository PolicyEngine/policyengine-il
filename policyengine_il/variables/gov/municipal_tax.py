from policyengine_il.model_api import *


class municipal_tax(Variable):
    label = "municipal_tax"
    documentation = "Total municipal tax, before reductions"
    entity = Household
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"
    default_value = 4_800
