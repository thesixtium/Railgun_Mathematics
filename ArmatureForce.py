import math


def resistance(params):
    cross_sectional = math.pi * params["wire_radius"] * params["wire_radius"]
    return params["resistivity"] \
        * 2 \
        * (params["railgun_length"] + params["armature_width"]) \
        * (1 / cross_sectional)


def amperage(params, t):
    exponent = t / ((resistance(params) + params["additional_resistance"]) * params["capacitor_capacity"])
    return (params["initial_capacitor_voltage"] * math.exp(exponent)) \
        / (resistance(params) + params["additional_resistance"])


def magnetic_force_on_armature(params, t):
    term1 = params["mu_0"]\
        * (1 / math.pi)\
        * amperage(params, t)\
        * amperage(params, t)
    term2 = math.log(params["armature_width"] + params["wire_radius"])\
        - math.log(params["wire_radius"])
    return term1 * term2
