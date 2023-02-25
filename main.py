import numpy as np
from Optimization import build_test
from Graphing import optimization_graph
from Kinematics import simulate_projectile
from Parameters import optimization_parameters, params


def make_param_set(lowest, highest, steps):
    return np.linspace(lowest, highest, steps).tolist()


def main():
    results = simulate_projectile(params)

    test = build_test(
        optimization_parameters["x_variable_name"],
        optimization_parameters["x_variable_points"],
        optimization_parameters["x_variable_minimum"],
        optimization_parameters["x_variable_maximum"],

        optimization_parameters["y_variable_name"],
        optimization_parameters["y_variable_points"],
        optimization_parameters["y_variable_minimum"],
        optimization_parameters["y_variable_maximum"],

        optimization_parameters["z_variable_name"],
        params,
        results
    )

    optimization_graph(test)


if __name__ == '__main__':
    main()
