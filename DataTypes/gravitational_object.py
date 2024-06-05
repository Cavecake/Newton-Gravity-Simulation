import numpy as np
import GravityFormulars
import math

class MassObject():
    def __init__(self, mass, radius, velocity, position) -> None:
        self.mass = np.array(mass)
        self.radius = np.array(radius)
        self.velocity = np.array(velocity)
        self.position = np.array(position)

    def set_velocity(self,new_velocity):
        self.velocity = new_velocity

    def set_mass(self,new_mass):
        self.mass = new_mass

    def set_position(self,new_position):
        self.position = new_position

    def set_radius(self,new_radius):
        self.radius = new_radius

    def addVelocity(self, deltaV):
        self.velocity = self.velocity + deltaV

    def addPosition(self, deltaPos):
        self.position = self.position + deltaPos

    def calc_relativistic_mass(self):
        m = self.mass
        gamma = self.calc_gamma()
        return m / gamma

    def calc_gamma(self):
        v = GravityFormulars.magnitude(self.velocity)
        c = GravityFormulars.C
        gamma = (v * v) / (c * c)
        gamma = math.sqrt(1 - gamma)
        return gamma