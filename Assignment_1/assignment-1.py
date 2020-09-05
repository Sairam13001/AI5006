# Given two parallel planes P1: a1 * x + b1 * y + c1 * z + d1 = 0 and P2: a2 * x + b2 * y + c2 * z + d2 = 0.
# This is a program to find distance between these planes
# Distance = (| a*x1 + b*y1 + c*z1 + d |) / (sqrt( a*a + b*b + c*c))

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Program for plotting the two parallel planes
a1,b1,c1,d1 = 2,3,4,4
a2,b2,c2,d2 = 4,6,8,12

x = np.linspace(-1,1,20)
y = np.linspace(-1,1,20)

X,Y = np.meshgrid(x,y)
Z1 = (d1 - a1*X - b1*Y) / c1
Z2 = (d2 - a2*X - b2*Y) / c2

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

surf1 = ax.plot_surface(X, Y, Z1)
surf2 = ax.plot_surface(X, Y, Z2)

plt.title('Assignment-1 : Parallel Planes')
plt.show()

#Program for finding the distance
def find_distance_bw_planes(a1,b1,c1,d1,a2,b2,c2,d2):
    #To check if planes are parallel
    if (a1/a2 == b1/b2 == c1/c2):
        #consider y1 = z1 = 0
        x1 = -d1/a1
        distance = abs(a2*x1 + d2)/sqrt(a2*a2+b2*b2+c2*c2)
    else:
        print("The given planes are not parallel")
        return -1
    return distance

print("The distance between the given parallel planes is : ", find_distance_bw_planes(2,3,4,-4,4,6,8,-12))
