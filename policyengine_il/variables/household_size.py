from policyengine_il.model_api import *


class household_size(Variable):
    label = "Household size"
    documentation = "Size of a household"
    entity = Household
    definition_period = YEAR
    value_type = int
    unit = "person"
