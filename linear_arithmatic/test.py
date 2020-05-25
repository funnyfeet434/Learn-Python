import numpy as np
import math

mag_v = int(input('What is the magnitude of v? '))
ang_v = int(input('what is the angle of v? '))
mag_w = int(input('What is the magnitude of w? '))
ang_w = int(input('what is the angle of w? '))


vector_v = np.array([round(np.cos(np.radians(ang_v))*mag_v, 2), round(np.sin(np.radians(ang_v))*mag_v, 2)])
vector_w = np.array([round(np.cos(np.radians(ang_w))*mag_w, 2), round(np.sin(np.radians(ang_w))*mag_w, 2)])

solution = vector_v + vector_w


print('Vector v is {0} and vector w is {1}.'.format(vector_v, vector_w))
print('The sum of v and w is ' + str(solution))
print('The magnitue of the solution is ' + str(round(np.sqrt(np.power(solution[0], 2)+np.power(solution[1], 2)), 2)))
print('The direction of the solution is ' + str(round(math.degrees(np.arctan(solution[1]/solution[0])), 2)))