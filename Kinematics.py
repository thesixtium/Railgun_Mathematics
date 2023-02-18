from ArmatureForce import magnetic_force_on_armature


def exit_velocity(params):
    current_velocity = 0
    current_distance = 0
    time = 0

    while current_distance < params["railgun_length"] and time < 0.07:
        force = magnetic_force_on_armature(params, time)
        acceleration = force / params["projectile_weight"]

        instant_velocity = acceleration * params["time_resolution"]
        current_velocity += instant_velocity

        current_distance += current_velocity * params["time_resolution"]

        time += params["time_resolution"]

    return current_velocity
