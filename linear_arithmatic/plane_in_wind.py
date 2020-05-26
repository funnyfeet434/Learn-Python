import math
import numpy as np 

def in_upper_quadrants(vector_2d):
    result = False
    if vector_2d[1]>0: result = True
    return result

v_b1 = np.array([400, 100])
v_b2 = np.array([350, 50])

wind_v1 = np.sqrt(v_b1[0]**2 + v_b1[1])
wind_v2 = np.sqrt(v_b2[0]**2 + v_b2[1])
dif_v1nv2 = v_b2 - v_b1
wind_speed = np.sqrt(dif_v1nv2[0]**2 + dif_v1nv2[1]**2)
if in_upper_quadrants(dif_v1nv2):
    wind_direction = np.arctan(dif_v1nv2[1]/dif_v1nv2[0])
else:
    wind_direction = np.arctan(dif_v1nv2[1]/dif_v1nv2[0])+np.pi


print('The speed of the wind is {0} km/h.'.format(round(wind_speed, 1)))
print('The direction of the wind is {0} degrees.'.format(round(wind_direction,2)))



