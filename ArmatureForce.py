import math
from math import sin
import matplotlib.pyplot as plt
# https://uio-ccse.github.io/computational-essay-showroom/essays/exampleessays/railgun_TOO/Railgun_V1_9.html


def resistance(params):
    rectangle = params["rail_height"] * params["rail_width"]
    circle = math.pi * pow(params["rail_width"]/2, 2)
    cross_sectional = rectangle + circle

    return params["resistivity"] \
        * 2 \
        * (params["railgun_length"] + params["armature_width"]) \
        * (1 / cross_sectional)


def magnetic_force_on_armature(params):
    time = 0
    velocity = 0
    armature_position = 0
    current = params["initial_capacitor_voltage"] / 0.001

    time_array = []
    velocity_array = []
    current_array = []
    armature_position_array = []

    f_net_array = []

    while armature_position < params["railgun_length"]:
        natural_log_term = math.log(params["armature_width"] + (params["rail_width"] / 2)) - math.log(
            params["rail_width"] / 2)

        # Inductance that causes current loss
        induced_current = params["2mu_over_2pi"] * current * natural_log_term * velocity
        current -= induced_current

        # Calculate Kinematics
        f_drag = params["frictional_coefficient"] * params["projectile_weight"] * 9.81 * sin(params["launch_angle"])
        f_magnet = params["2mu_over_2pi"] * pow(current, 2) * natural_log_term
        f_net = f_magnet - f_drag
        velocity += (f_net/params["projectile_weight"]) * params["time_step"]
        armature_position += velocity * params["time_step"]

        # Array Updates
        time_array.append(time)
        velocity_array.append(velocity)
        f_net_array.append(f_net)
        current_array.append(current)
        armature_position_array.append(armature_position)

        time += params["time_step"]

        if time > 2:
            return {
                "time_array": [0],
                "armature_position_array": [0],
                "velocity_array": [0],
                "f_net_array": [0],
                "current_array": [0]
            }

    return {
        "time_array": time_array,
        "armature_position_array": armature_position_array,
        "velocity_array": velocity_array,
        "f_net_array": f_net_array,
        "current_array": current_array
    }


def plot_magnetic_force_on_armature(params):
    results = magnetic_force_on_armature(params)

    fig, ax = plt.subplots(nrows=2, ncols=2)

    ax[0, 0].set_title("Time vs Position")
    ax[0, 0].plot(results["time_array"], results["armature_position_array"], color="black")[0]

    ax[0, 1].set_title("Time vs Velocity (m/s)")
    ax[0, 1].plot(results["time_array"], results["velocity_array"], color="black")[0]

    ax[1, 0].set_title("Time vs Current")
    ax[1, 0].plot(results["time_array"], results["current_array"], color="black")[0]

    ax[1, 1].set_title("Time vs f_net")
    ax[1, 1].plot(results["time_array"], results["f_net_array"], color="black")[0]

    plt.show()