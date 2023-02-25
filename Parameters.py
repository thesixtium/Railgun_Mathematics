import math

params = {
        # meters
        "railgun_length": 1,
        "armature_width": 0.15,
        "rail_width": 0.1,
        "rail_height": 0.01,

        # kg
        "projectile_weight": 0.355,

        # ohm-meter
        "resistivity": 1.68 * pow(10, -8),

        # volts
        "initial_capacitor_voltage": 100,

        # Time resolution
        "time_step": 0.0001,

        # Netwons
        "initial_force": 100,

        # No units
        "frictional_coefficient": 0.08,
        "2mu_over_2pi": 4 * pow(10, -7),
        "launch_angle": 45 * (math.pi / 180)
    }

optimization_parameters = {
    "x_variable_name": "projectile_weight",
    "x_variable_points": 2,
    "x_variable_minimum": 0.1,
    "x_variable_maximum": 1,

    "y_variable_name": "initial_capacitor_voltage",
    "y_variable_points": 2,
    "y_variable_minimum": 0.1,
    "y_variable_maximum": 1,

    "z_variable_name": "x_velocity",
}
