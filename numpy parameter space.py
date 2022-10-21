import numpy as np
import matplotlib.pyplot as plt
from numpy import cfloat
import math
import datetime

i=1j ##numpy uses j for the imaginary unit, I define i to not get confused

def f(z, z_0): ##This is the functionn we are iterating. z_0 is the point in the complex plane, and z is 
    return np.exp(z)+z_0

escape_limit = 2 #This is the radius that we define the escape algorithm with

zoom = 1#/10
x_offset = 0 ##The centre of the plot will be on (x_offset,y_offset)
y_offset = 0

left_lim, right_lim = -2/zoom+x_offset , 2/zoom+x_offset ##defines the boundaries of the graph
lower_lim, upper_lim = -2/zoom+y_offset, 2/zoom+y_offset

resolution = 1000 #defines the number of pixels in the image
iterations = 100#0 #defined the max. number of iterations we carry out

reals = np.linspace(left_lim, right_lim, resolution+1, dtype = cfloat)
ims = np.linspace(upper_lim, lower_lim, resolution+1, dtype = cfloat)

coords = np.meshgrid(reals, ims)
z_0 = coords[0]+i*coords[1]
z=z_0

escape_array = np.zeros(z.shape)
##escape array will be an array where each element is an integer which tells
##how many iterations it takes before the corresponding value has an absolute
##value greater than escape_limit

for i in range(iterations):
    print(i)
    z=f(z, z_0)
    new_bool = (np.abs(z) <= escape_limit)
    escape_array+=new_bool

plt.imshow(np.dstack((np.floor(255*np.sin(escape_array*0.03)**2),
                      np.floor(255*np.sin(escape_array*0.03+(1/3)*np.pi)**2),
                      np.floor(255*np.sin(escape_array*0.03+(2/3)*np.pi)**2))).astype(int),
           extent=(left_lim, right_lim, lower_lim, upper_lim))  ##This will produce a rainbow coloured image

##plt.imshow(escape_array, extent=(left_lim, right_lim, lower_lim, upper_lim))
##plt.colorbar() ##This will produce a blue/green/yellow coloured graph by default, but the colour scheme can be changed

plt.show()
