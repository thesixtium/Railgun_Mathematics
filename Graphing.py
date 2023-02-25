import matplotlib.pyplot as plt
from Optimization import find_best_parameters_of_two_variables
from ArmatureForce import magnetic_force_on_armature


def optimization_graph(test):
    optimization_results = find_best_parameters_of_two_variables(test)
    projectile_sims_results = optimization_results["best"][0]
    magnetic_results = magnetic_force_on_armature(optimization_results["best"][4])

    fig, axs = plt.subplot_mosaic(
        [['3d_scatter', '3d_scatter', 'projectile_flight', 'projectile_flight'],
         ['3d_scatter', '3d_scatter', 'projectile_flight', 'projectile_flight'],
         ['3d_scatter', '3d_scatter', 'velocity', 'current']],
        constrained_layout=True,
        per_subplot_kw={
            "3d_scatter": {"projection": "3d"}
        }
    )

    axs['3d_scatter'].scatter3D(
        optimization_results["x_values"],
        optimization_results["y_values"],
        optimization_results["z_values"],
        color="green"
    )
    axs['3d_scatter'].set_xlabel(optimization_results["x_label"], fontweight='bold')
    axs['3d_scatter'].set_ylabel(optimization_results["y_label"], fontweight='bold')
    axs['3d_scatter'].set_zlabel(optimization_results["z_label"], fontweight='bold')
    plt.title("{} vs {} vs {}".format(
        optimization_results["x_label"],
        optimization_results["y_label"],
        optimization_results["z_label"]
    ))

    axs['projectile_flight'].plot(projectile_sims_results["time"], projectile_sims_results["y_pos"], color="black")[0]
    axs['velocity'].plot(magnetic_results["time_array"], magnetic_results["velocity_array"], color="black")[0]
    axs['current'].plot(magnetic_results["time_array"], magnetic_results["current_array"], color="black")[0]

    axs['3d_scatter'].set_title('Parameter Optimization')
    axs['projectile_flight'].set_title('Projectile Flight Path')
    axs['velocity'].set_title('In-Barrel Velocity')
    axs['current'].set_title('Railgun Current')

    plt.show()
