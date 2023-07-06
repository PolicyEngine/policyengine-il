from policyengine_il.model_api import *


class max_low_income_municipal_tax_reduction(Variable):
    label = "Maximum low-income municipal tax reduction"
    documentation = (
        "Municipalities can reduce municipal tax by up to this amount"
    )
    entity = Household
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"
    reference = "https://www.kolzchut.org.il/he/%D7%94%D7%A0%D7%97%D7%94_%D7%91%D7%90%D7%A8%D7%A0%D7%95%D7%A0%D7%94_%D7%9C%D7%91%D7%A2%D7%9C%D7%99_%D7%94%D7%9B%D7%A0%D7%A1%D7%94_%D7%A0%D7%9E%D7%95%D7%9B%D7%94"

    def formula(household, period, parameters):
        reduction_rate = household(
            "max_low_income_municipal_tax_reduction_rate", period
        )
        municipal_tax = household("municipal_tax", period)
        return reduction_rate * municipal_tax
