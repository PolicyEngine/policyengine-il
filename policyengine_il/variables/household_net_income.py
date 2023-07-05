from policyengine_il.model_api import *


class household_net_income(Variable):
    label = "net income"
    entity = Household
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"
    adds = ["household_market_income", "household_benefits"]
    subtracts = ["household_tax"]
