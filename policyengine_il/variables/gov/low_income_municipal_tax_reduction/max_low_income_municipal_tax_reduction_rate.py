from policyengine_il.model_api import *


class max_low_income_municipal_tax_reduction_rate(Variable):
    label = "Maximum low-income municipal tax reduction rate"
    documentation = (
        "Municipalities can reduce municipal tax by up to this percentage"
    )
    entity = Household
    definition_period = YEAR
    value_type = float
    unit = "/1"
    reference = "https://www.kolzchut.org.il/he/%D7%94%D7%A0%D7%97%D7%94_%D7%91%D7%90%D7%A8%D7%A0%D7%95%D7%A0%D7%94_%D7%9C%D7%91%D7%A2%D7%9C%D7%99_%D7%94%D7%9B%D7%A0%D7%A1%D7%94_%D7%A0%D7%9E%D7%95%D7%9B%D7%94"

    def formula(household, period, parameters):
        params = parameters(period).gov.low_income_municipal_tax_reduction_rate
        annual_income = household(
            "low_income_municipal_tax_reduction_income", period
        )
        monthly_income = annual_income / MONTHS_IN_YEAR
        household_size = household("household_size", period)
        rates = np.zeros_like(monthly_income)
        for possible_household_size in range(1, 10):
            applicable_rate = getattr(
                params, str(possible_household_size)
            ).calc(monthly_income, right=True)
            rates = where(
                household_size == possible_household_size,
                applicable_rate,
                rates,
            )
        return rates
