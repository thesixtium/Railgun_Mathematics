# Railgun Mathematics

Railgun Mathematics is a Python software for simulating and optimizing railgun parameters before building. It allows predicted outcome simulations and the optimization of 2 parameters simultaneously.

## Installation

Clone this repository and make sure to install the following packages:
```bash
pip install matplotlib
pip install numpy
```
This was made in Python 3.8, but I would be surprised if it didn't run in other versions of Python.

## Usage
### Running
I never run Python code from the command line, nor do I code in something super basic like Nano or IDLE. I code in PyCharm, and therefore launch via the run button. Run this software from the main file. It launches from the following code snippet at the bottom of the file:
```python
if __name__ == '__main__':
    main()
```

### Modifying Parameters
To edit parameters, edit the Parameters.py file. Everything in the params dictionary is the basic railgun parameters, and everything in the optimization_parameters dictionary is to set up the optimization simulations.
#### Params
Parameters are sorted by their unit (meters, kg, etc)
* railgun_length: Length of one of the railgun's rails
* armature_width: How wide the projectile is (can also be interpreted as the width between the rails)
* rail_width: Width of one of the rails
* rail_height: How thick each rail is
* projectile_weight: How heavy the fired projectile is
* resistivity: the resistance of the metal used for the rails (currently set to Copper)
* initial_capacitor_voltage: The voltage the capacitors are initially charged to
* time_step: During simulations, how often to sample the variables (so with a time_step of 1, the simulation will take data points every 1 second [0, 1, 2] but with a time_step of 0.1 the simulation will take data points every 0.1 seconds [0, 0.1, 0.2])
* initial_force: How much force the projectile initially has before coming into contact with the rails (if you start with 0 the simulation won't care, but in real life the projectile will just weld itself to the rails)
* frictional_coefficient: The frictional coefficient between the rails and the projectile / armeture (currently at the frictional coefficient between copper and copper)
* 2mu_over_2pi: A constant in electrical engineering, precalculating it speeds up everything
* launch_angle: The angle of launch of the railgun in radians. 0 * (math.pi / 180) is parallel to the ground, and 90 * (math.pi / 180) is straight up into the air

## Contributing

Please do whatever you'd like with it as long as you stay safe and remain within the law. Pull requests are welcome but I also don't check my pull requests ever so please just clone and cite this repository

## Contact
[My Website](https://thesixtium.github.io/)

## License
[MIT](https://choosealicense.com/licenses/mit/)
