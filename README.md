# Newton-Gravity-Simulation
 
This is a simple implementation of a gravity simulation using the LeapFrog integration scheme.

To initialise a simulation with a GUI edit 
```
bodies = [
    {"m": 1.898e30, "r": 2, "v": [0, 0], "pos": [0, 0]},
    {"m": 5.9772e24, "r": 2, "v": [29780, 0], "pos": [0, 149600000000]}
]
```

inside GUI_Gravity and run the script. 
- m is the mass in kgs
- r is the radius of the object (irrelevant)
- v is the velocity vector at the start of the simulation
- pos the position at the start of the simulation

## Background calculations

To calculate the positions in the background run LeapFrog.py from DataTypes.
This also includes the bodies list, with the same types of data. 