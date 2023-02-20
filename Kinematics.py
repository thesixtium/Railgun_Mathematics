from math import cos, sin
import math
import matplotlib.pyplot as plt
from ArmatureForce import magnetic_force_on_armature

def simulate_projectile(params, printout=False):
    results = magnetic_force_on_armature(params)

    time = 0
    time_array = []

    x_pos = 0
    y_pos = 2  # Assume fired from 2m up

    x_pos_array = []
    y_pos_array = []

    x_velocity = results["velocity_array"][-1] * cos(params["launch_angle"])
    y_velocity = results["velocity_array"][-1] * sin(params["launch_angle"])

    x_velocity_array = []
    y_velocity_array = []

    while y_pos > 0:
        y_velocity -= 9.81 * params["time_step"]

        x_pos += x_velocity
        y_pos += y_velocity

        x_pos_array.append(x_pos)
        y_pos_array.append(y_pos)
        x_velocity_array.append(x_velocity)
        y_velocity_array.append(y_velocity)
        time_array.append(time)

        time += params["time_step"]

    if printout:
        string_precision = 35
        print("\nInput Statistics")
        print(("Voltage:                {}".format(params["initial_capacitor_voltage"]))[0:string_precision] + " V")
        print(("Resistance:             {}".format(0.001))[0:string_precision] + " Ohms")
        print(("Current:                {}".format(params["initial_capacitor_voltage"] / 0.001))[0:string_precision] + " A")
        print(("Railgun Length:         {}".format(params["railgun_length"]))[0:string_precision] + " m")
        print(("Width of Each Rail:     {}".format(params["rail_width"]))[0:string_precision] + " m")
        print(("Projectile Width:       {}".format(params["armature_width"]))[0:string_precision] + " m")
        print(("Projectile Weight:      {}".format(params["projectile_weight"]))[0:string_precision] + " kg")
        print(("Launch Angle:           {}".format(params["launch_angle"] * (180/math.pi)))[0:string_precision] + " degrees")

        print("\nOut of Barrel Statistics")
        print(("Out Of Barrel Time:     {}".format(results["time_array"][-1]))[0:string_precision] + " s")
        print(("Out Of Barrel Velocity: {}".format(results["velocity_array"][-1]))[0:string_precision] + " m/s")
        print(("Out Of Barrel Velocity: {}".format(results["velocity_array"][-1] * 3.6))[0:string_precision] + " km/h")

        print("\nLaunch Statistics")
        print(("Maximum Height:         {}".format(max(y_pos_array)))[0:string_precision] + " m")
        print(("Maximum Height:         {}".format(max(y_pos_array) / 1000))[0:string_precision] + " km")
        print(("Distance Launched:      {}".format(x_pos_array[-1] * 3.6))[0:string_precision] + " m")
        print(("Distance Launched:      {}".format((x_pos_array[-1] * 3.6) / 1000))[0:string_precision] + " km")

    return {
        "x_pos": x_pos_array,
        "y_pos": y_pos_array,
        "x_velocity": x_velocity_array,
        "y_velocity": y_velocity_array,
        "time": time_array
    }

def plot_simulate_projectile(params):
    results = simulate_projectile(params)

    fig, ax = plt.subplots(nrows=2, ncols=2)

    ax[0, 0].set_title("Time vs X Position")
    ax[0, 0].plot(results["time"], results["x_pos"], color="black")[0]

    ax[0, 1].set_title("Time vs Y Position")
    ax[0, 1].plot(results["time"], results["y_pos"], color="black")[0]

    ax[1, 0].set_title("Time vs X Velocity")
    ax[1, 0].plot(results["time"], results["x_velocity"], color="black")[0]

    ax[1, 1].set_title("Time vs Y Velocity")
    ax[1, 1].plot(results["time"], results["y_velocity"], color="black")[0]

    plt.show()