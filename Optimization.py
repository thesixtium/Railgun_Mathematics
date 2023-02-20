import numpy as np
import matplotlib.pyplot as plt
from Kinematics import simulate_projectile

def build_test(
        variable1, variable1_points, variable1_min, variable1_max,
        variable2, variable2_points, variable2_min, variable2_max,
        goal, params, results, printout=False):

    # Merge Dictionaries
    data = {}
    for key in params:
        data[key] = params[key]

    for key in results:
        data[key] = results[key]

    test = {
        # Parameter Variable 1 - X Variable
        "x": variable1,
        "x_points": variable1_points,
        "x_min": variable1_min,
        "x_max": variable1_max,

        # Parameter Variable 1 - X Variable
        "y": variable2,
        "y_points": variable2_points,
        "y_min": variable2_min,
        "y_max": variable2_max,

        "z": goal,
        "data": data,
        "params": params
    }

    if printout:
        print('\ntest["x"]: ' + str(test["x"]))
        print('test["x_points"]: ' + str(test["x_points"]))
        print('test["x_min"]: ' + str(test["x_min"]))
        print('test["x_max"]: ' + str(test["x_max"]))

        print('test["y"]: ' + str(test["y"]))
        print('test["y_points"]: ' + str(test["y_points"]))
        print('test["y_min"]: ' + str(test["y_min"]))
        print('test["y_max"]: ' + str(test["y_max"]))

        print('test["z"]: ' + str(test["z"]))
        print('test["data"]')
        for key in data:
            print('\tdata["{}"]: '.format(key))

    return test

def find_best_parameters_of_two_variables(test):
    x_test_values = np.linspace(test["x_min"], test["x_max"], test["x_points"]).tolist()
    y_test_values = np.linspace(test["y_min"], test["y_max"], test["y_points"]).tolist()

    x_values = []
    y_values = []
    z_values = []

    current_best = [0, 0, 0, 0]

    for x in x_test_values:
        print("On simulation {} of {} (len(x): {}\tlen(y): {})".format(
            len(z_values),
            len(x_test_values) * len(y_test_values),
            len(x_values),
            len(y_values),
        ))

        for y in y_test_values:
            test["params"][test["x"]] = x
            test["params"][test["y"]] = y

            projectile_sim = simulate_projectile(test["params"])
            z = projectile_sim[test["z"]][-1]

            if z > current_best[3]:
                current_best[0] = projectile_sim
                current_best[1] = x
                current_best[2] = y
                current_best[3] = z

            x_values.append(x)
            y_values.append(y)
            z_values.append(z)

    print("Best: ")
    print("\tx ({}): {}".format(
        test["x"],
        current_best[1]
    ))
    print("\ty ({}): {}".format(
        test["y"],
        current_best[2]
    ))
    print("\tz ({}): {}".format(
        test["z"],
        current_best[3]
    ))

    return {
        "x_values": x_values,
        "x_label": test["x"],
        "y_values": y_values,
        "y_label": test["y"],
        "z_values": z_values,
        "z_label": test["z"],
        "best": current_best
    }


def plot_find_best_parameters_of_two_variables(test):
    results = find_best_parameters_of_two_variables(test)

    # Creating figure
    fig = plt.figure(figsize=(10, 7))
    ax = plt.axes(projection="3d")

    # Creating plot
    ax.scatter3D(results["x_values"], results["y_values"], results["z_values"], color="green")
    ax.set_xlabel(results["x_label"], fontweight='bold')
    ax.set_ylabel(results["y_label"], fontweight='bold')
    ax.set_zlabel(results["z_label"], fontweight='bold')
    plt.title("{} vs {} vs {}".format(
        results["x_label"],
        results["y_label"],
        results["z_label"]
    ))

    # show plot
    plt.show()