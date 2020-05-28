import math
import numpy as np

def in_upper_quadrants(vector_2d):
    result = False
    if vector_2d[1]>0: result = True
    return result

v_b1 = np.array([100, 10])
v_b2 = np.array([90, -20])

distance_b1 = np.sqrt(v_b1[0]**2 + v_b1[1]**2)
distance_b2 = np.sqrt(v_b2[0]**2 + v_b2[1]**2)
distance_diff = abs(distance_b1 - distance_b2)

difference_balls = v_b2 - v_b1
distance_balls = np.sqrt(difference_balls[0]**2 + difference_balls[1]**2)


print('Ball 1 was thrown {0}m further than ball 2'.format(round(distance_diff, 1)))
print('The balls are {0}m apart from each other'.format(round(distance_balls,1)))



