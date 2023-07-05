from policyengine_il.model_api import *


class tax(Variable):
    label = "individual tax"
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-ILS"

    def formula(person, period, parameters):
        exempt = person("is_tax_exempt", period)
        main_rates = person("main_tax_rates", period)
        minimum_tax = person("minimum_tax", period)
        return ~exempt * max_(main_rates, minimum_tax)
