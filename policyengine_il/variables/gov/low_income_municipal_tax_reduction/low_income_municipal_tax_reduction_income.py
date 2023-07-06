from policyengine_il.model_api import *


class low_income_municipal_tax_reduction_income(Variable):
    label = "Low-income municipal tax reduction income"
    documentation = "Municipalities base their municipal tax reduction rate on this income"
    entity = Household
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"
    adds = [
        "employment_income",
        "self_employment_income",
        "pension_income",
    ]