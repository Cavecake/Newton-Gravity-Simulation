if __name__ == "__main__":
    import os
    import sys
    os.chdir(os.path.dirname(os.path.dirname(__file__)))
    sys.path.append(os.getcwd())

from DataTypes.gravitational_object import MassObject
import DataTypes.GravityFormulars as GravityFormulars
import warnings
import numpy as np
import copy
import pandas as pd

def initialize_log(file_name, num_planets):
    columns = ["x" + str(i) for i in range(num_planets)] + ["y" + str(i) for i in range(num_planets)]
    df = pd.DataFrame(columns=columns)
    df.to_csv(file_name, index=False)

# Append data to the CSV file
def log_positions(file_name, data):
    num_planets = len(data)
    x_columns = ["x" + str(i) for i in range(num_planets)]
    y_columns = ["y" + str(i) for i in range(num_planets)]

    data_dir = {x_columns[i]: float(data[i][0]) for i in range(num_planets)}
    data_dir.update({y_columns[i]: float(data[i][1]) for i in range(num_planets)})

    df = pd.DataFrame([data_dir])
    df.to_csv(file_name, mode='a', header=False, index=False)

class LeapFrog_Gravity_Sim():
    def __init__(self, bodies, step_size, Log = False, LogFile = "") -> None:
        if not isinstance(bodies,list):
            raise TypeError("Bodies must be a list of MassObjects")
        if not isinstance(bodies[0],MassObject):
            raise TypeError("Using invalid type for gravitational body")
        if not isinstance(step_size,(int,float)):
            raise TypeError("Step Size should be a float")
        if isinstance(step_size,int):
            warnings.warn("You should consider using a step_size less than one")
        self.bodies = bodies
        self.step_size = step_size

        self.Log = Log
        self.LogFile = LogFile

        if Log:
            initialize_log(LogFile,len(self.bodies))

    def step(self):
        body1 : MassObject
        body2 : MassObject
        accelerations = []
        positions = []
        for i, body1 in enumerate(self.bodies):
            start_pos = body1.get_position()
            start_v = body1.get_velocity()



            force = np.array((0,0), dtype=np.float64)
            for j, body2 in enumerate(self.bodies):
                if i != j:
                    force_vector = body2.get_position() - body1.get_position()
                    distance = GravityFormulars.calc_distance(body1.get_position(), body2.get_position())
                    force += GravityFormulars.calc_force(body1.get_mass(),body2.get_mass(), distance, force_vector)
            acceleration = GravityFormulars.calc_acceleration(force, body1.get_mass())
            accelerations.append(acceleration)
            # Calculate next Position
            next_pos = start_pos
            next_pos = np.array(next_pos) + np.array(start_v * self.step_size)
            next_pos += np.array(acceleration * (self.step_size * self.step_size) * 0.5)
            positions.append(next_pos)

        if self.Log:
            log_positions(self.LogFile,positions)

        for i, body1 in enumerate(self.bodies):
            body1.set_position(positions[i])

        for i, body1 in enumerate(self.bodies):
            start_v = body1.get_velocity()

            force = np.array((0,0), dtype=np.float64)
            for j, body2 in enumerate(self.bodies):
                if i != j:
                    distance = GravityFormulars.calc_distance(body1.get_position(), body2.get_position())
                    force_vector = body2.get_position() - body1.get_position()
                    force += GravityFormulars.calc_force(body1.get_mass(),body2.get_mass(), distance, force_vector)
            new_acceleration = GravityFormulars.calc_acceleration(force, body1.get_mass())

            old_acceleration = accelerations[i]
            # Calculate next velocity
            next_velocity = start_v
            next_velocity += 0.5 * (old_acceleration + new_acceleration) * self.step_size
            body1.set_velocity(next_velocity)


    def predict(self,steps, step_size):
        positions = []
        bodies = copy.deepcopy(self.bodies)

        old_steps = self.step_size
        self.step_size = step_size

        for i in self.bodies:
            positions.append([])
        for step in range(steps):
            self.step()
            for i, body in enumerate(self.bodies):
                position = body.get_position()
                position = [float(x) for x in position]
                positions[i].append(position)

        self.bodies = copy.deepcopy(bodies)
        self.step_size = old_steps
        return positions

    def get_body_positions(self):
        positions = []
        for body in self.bodies:
            positions.append(body.get_position())
        return positions
# x2 = x1 + v1*dt + a(x1) * dt^2 / 2
# v2 =  v1 + (a(x2) + a(x1)) dt/2

if __name__ == "__main__":
    import tqdm



    STEP_SIZE = 1
    RUNTIME = 86000 * 365
    bodies = [
        {"m": 1.898e30, "r": 2, "v": [0, 0], "pos": [0, 0]},
        {"m": 5.9772e24, "r": 2, "v": [29780, 0], "pos": [0, 149600000000]}

    ]

    mass_bodies = []
    for body in bodies:
        mass_bodies.append(MassObject(body["m"], body["r"], body["v"], body["pos"]))

    sim = LeapFrog_Gravity_Sim(mass_bodies, STEP_SIZE,Log = True, LogFile = "DataTypes/log.csv")

    progress = tqdm.tqdm(total = RUNTIME)

    for step in range(RUNTIME):
        sim.step()
        progress.update()