import numpy as np 
import matplotlib as mpl 

x = np.linspace(0, 1, 100)
y = np.sin(x)
np.plot(x, y)
np.show()