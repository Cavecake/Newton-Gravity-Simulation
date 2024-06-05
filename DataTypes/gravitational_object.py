import numpy as np
import GravityFormulars
import math

class MassObject():
    def __init__(self, mass, radius, velocity, position) -> None:
        self.check_vector(position)
        self.check_vector(position)
        if not isinstance(mass,[int,float]):
            raise TypeError("Mass must be a number")
        if not isinstance(radius,[int,float]):
            raise TypeError("Radius must be a number")
        
        self.mass = np.array(mass)
        self.radius = np.array(radius)
        self.velocity = np.array(velocity)
        self.position = np.array(position)

    def check_vector(self,input_data):
        if not isinstance(input_data,[list,np.array]):
            raise TypeError("Velocity must be a Vector (list of ints)")
        
        for elem in input_data:
            if not isinstance(elem,[int,float]):
                raise TypeError("Velocity must be a Vector (list of ints)")

    def set_velocity(self,new_velocity):
        self.check_vector(new_velocity)
        self.velocity = new_velocity

    def set_mass(self,new_mass):
        if not isinstance(new_mass,[int,float]):
            raise TypeError("Mass must be a number")
        self.mass = new_mass

    def set_position(self,new_position):
        self.check_vector(new_position)
        self.position = new_position

    def set_radius(self,new_radius):
        if not isinstance(new_radius,[int,float]):
            raise TypeError("Radius must be a number")
        self.radius = new_radius

    def addVelocity(self, deltaV):
        self.check_vector(deltaV)
        self.velocity = self.velocity + deltaV

    def addPosition(self, deltaPos):
        self.check_vector(deltaPos)
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