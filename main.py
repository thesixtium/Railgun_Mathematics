import math
import numpy as np
from Kinematics import simulate_projectile
from Optimization import build_test, plot_find_best_parameters_of_two_variables


# Math for a can cannon rail gun

# TODO:
#   Resistance + Additional resistance
#   Clean up all parameters not using
#   List of all parameters to optimize
#   Way to optimize parameters within a range

def build_params():
    params = {
        # meters
        "railgun_length": 1,
        "armature_width": 0.15,
        "rail_width": 0.1,
        "rail_height": 0.01,

        # kg
        "projectile_weight": 0.355,

        # ohms
        "additional_resistance": 0,

        # ohm-meter
        "resistivity": 1.68 * pow(10, -8),

        # farads
        "capacitor_capacity": 1000,

        # volts
        "initial_capacitor_voltage": 100,

        # H/m
        "mu_0": math.pi * 4 * pow(10, -7),

        # Time resolution
        "time_step": 0.0001,

        # Netwons
        "initial_force": 100,

        # No units
        "frictional_coefficient": 0.08,
        "2mu_over_2pi": 4 * pow(10, -7),
        "launch_angle": 45 * (math.pi / 180)
    }

    return params


def make_param_set(lowest, highest, steps):
    return np.linspace(lowest, highest, steps).tolist()


def main():
    params = build_params()
    results = simulate_projectile(params)

    test = build_test(
        "projectile_weight", 10, 0.1, 1,
        "initial_capacitor_voltage", 10, 2, 400,
        "x_velocity", params, results
    )

    plot_find_best_parameters_of_two_variables(test)


if __name__ == '__main__':
    main()
