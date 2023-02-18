import math
from Kinematics import exit_velocity

# Math for a can cannon rail gun

def build_params():
    params = {
        # meters
        "wire_radius": 0.1,
        "railgun_length": 1,
        "armature_width": 0.01,

        # kg
        "projectile_weight": 0.355,

        # ohms
        "additional_resistance": 100,

        # ohm-meter
        "resistivity": 1.68 * pow(10, -8),

        # farads
        "capacitor_capacity": 1,

        # volts
        "initial_capacitor_voltage": 100,

        # H/m
        "mu_0": math.pi * 4 * pow(10, -7),

        # Time resolution
        "time_resolution": 0.0001
    }

    return params

def main():
    print(exit_velocity(build_params()))


if __name__ == '__main__':
    main()
