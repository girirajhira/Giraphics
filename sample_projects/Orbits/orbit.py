# from Scenic import *
# from convert import *
# import numpy as np
#
# frames = 250 + 1
# create_directory("ftp")
# create_directory("ftprast")
#
# for i in range(frames):
#     t = i/20
#     # Setup
#     A = Scene(1980, 1080, 16, 9,"ftp/g"+namer(i)+".svg", origin=[0,0])
#     A.bg(colour="black")
#     g = Widget(10, 10, A, pos=[-8,0], scale=[0.5,1], origin=[-10,0])
#     # Graph
#     g.grid()
#     g.axes("yellow")
#     g.graph(yg(t), colour="yellow")
#     # Pendulum drawing
#     A.draw_rect(0,y(t), 1.5, 1.5, fill="white")
#     A.draw_line(0,0, 0, y(t), stroke="white")
#     A.draw_line(-8,y(t), 0, y(t), stroke="red")
#     # Savings
#     A.commitWidget(g)
#     A.save()
#
# # Converting SVG to PNG
# create_raster_batch("ftp", 'g', 'p', 'ftprast', frames)
# # Creating the final video
# create_mpeg('Springs4.mp4', 'p', frames, dir=os.getcwd()+"/ftprast", framerate=60)

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

M=1000
G=0.5
N = 10000
eps= .02
m = 1
def norm(x):
    total=0
    for i in x:
        total+=i**2
    return (total)**.5

# class point:
#     def __init__(self, r0, v0, mass):
#         self.r = r0
#         self.v = v0
#         self.mass = mass
#
#     def next(self, eps):
#         acc = -(G*M*self.mass/norm(self.r))*self.r
#         self.v += acc*eps
#         self.r += self.v*eps
#         return (self.r[0], self.r[1])

# X, Y = [], []
# p = point(np.array([0.,9.]), np.array([-.9,0.1]), 1)
# for i in range(100):
#     (x, y) = p.next(eps)
#     X.append(x)
#     Y.append(y)

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(state,t):
    x, y, vx, vy = state
    if x**2+y**2 != 0:
        dvx = -((G*m*M)/((x**2 + y**2)**3))*x
        dvy = -((G*m*M)/((x**2 + y**2)**3))*y
    else:
        dvx = 0
        dvy = 0
    return [vx, vy, dvx, dvy]

# initial condition
state0 = [-10,2,.15,.21]

# time points
t = np.arange(0,60, .5)

# solve ODE
sol = odeint(model,state0,t)
x, y = sol[:,0], sol[:,1]
# plot results
plt.plot(x,y)
plt.scatter([0], [0])
plt.xlabel('x')
plt.ylabel('y')
plt.show()