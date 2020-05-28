import math
import numpy as np 

v_b1 = np.array([400, 100])
v_b2 = np.array([350, 50])

distance_travelled_b1 = np.sqrt(v_b1[0]**2 + v_b1[1])
distance_travelled_b2 = np.sqrt(v_b2[0]**2 + v_b2[1])
dif_b1nb2 = abs(v_b1 - v_b2)
distance_b1nb2 = np.sqrt(dif_b1nb2[0]**2 + dif_b1nb2[1]**2)

print('The first ball travelled {0} m more.'.format(round(distance_travelled_b1-distance_travelled_b2, 1)))
print('The distance between the two balls is ' + str(round(distance_b1nb2, 1)))