from DataTypes.constant import Constants
import numpy as np
from scipy.spatial import distance
import math

G = Constants(6.67259,0.00085,-11)
C = 299792458

def check_is_vector(vector):
    if not isinstance(vector,(list,np.array)):
        raise TypeError("Velocity must be a Vector (list of ints)")
    
    for elem in vector:
        if not isinstance(elem,(int,float)):
            raise TypeError("Velocity must be a Vector (list of ints)")
def normalize(v):
    return np.array(v / np.sqrt(np.sum(v**2)), dtype=np.float64)

def calc_force(mass1, mass2, distance, direction_vector):
    if not isinstance(mass1, (int,float)):
        raise TypeError("Mass must be a number")
    if not isinstance(mass2, (int,float)):
        raise TypeError("Mass must be a number")
    if not isinstance(distance, (int,float)):
        raise TypeError("Distance must be a number")
    force = G * (mass1 * mass2)/(distance * distance)
    
    return force * normalize(direction_vector)

def calc_acceleration(force, mass):
    if not isinstance(mass, (int,float)):
        raise TypeError("Mass must be a number")
    acceleration = force / mass
    return acceleration

def calc_distance(point1, point2):
    return distance.euclidean(point1, point2)

def check_collision(point1, point2, radius1, radius2):
    if not isinstance(radius1, (int,float)):
        raise TypeError("Radius must be a number")
    if not isinstance(radius2, (int,float)):
        raise TypeError("Radius must be a number")
    
    check_is_vector(point1)
    check_is_vector(point2)

    if calc_distance(point1,point2) <= radius1 + radius2:
        return True
    return False

def magnitude(vector): 
    check_is_vector(vector)
    return math.sqrt(sum(pow(element, 2) for element in vector))