from DataTypes.constant import Constants
import numpy as np
from scipy.spatial import distance

G = Constants(6.67259,0.00085,-11)

def calc_force(mass1, mass2, distance):
    force = G * (mass1 * mass2)/(distance * distance)
    return force

def calc_acceleration(force, mass):
    acceleration = force / mass
    return acceleration

def calc_distance(point1, point2):
    return distance(point1, point2)

def check_collision(point1, point2, radius1, radius2):
    if calc_distance(point1,point2) <= radius1 + radius2:
        return True
    return False
