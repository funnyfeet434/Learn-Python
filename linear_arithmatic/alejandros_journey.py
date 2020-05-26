import math
import numpy as np 

def in_upper_quadrants(vector_2d):
    result = False
    if vector_2d[1]>0: result = True
    return result

v_d1 = np.array([3, 7])
v_d2 = np.array([-1, 8])

v_d3 = -(v_d1+v_d2)
distance_d3 = np.sqrt(v_d3[0]**2 + v_d3[1]**2)
if in_upper_quadrants(v_d3):
    travel_direction = np.arctan(v_d3[1]/v_d3[0])
else:
    travel_direction = np.degrees(np.arctan(v_d3[1]/v_d3[0])+np.pi)


print('Alejandro travelled {0} km on day 3.'.format(round(distance_d3, 1)))
print('The direction of travel n day 3 is {0} degrees.'.format(round(travel_direction,2)))



