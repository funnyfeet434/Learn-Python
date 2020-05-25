import numpy as np
import math
vector_v = np.array([np.cos(np.radians(100))*6, np.sin(np.radians(100))*6])
vector_w = np.array([np.cos(np.radians(40))*5, np.sin(np.radians(40))*5])

solution = vector_v + vector_w


print('Vector v is {0} and vector w is {1}.'.format(vector_v, vector_w))
print('The sum of v and w is ' + str(solution))

