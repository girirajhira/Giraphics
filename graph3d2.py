from svgwtr import *
from graph import *
from convert import *
from grapher import *
import numpy as np
from math import cos, sin




def Rz(theta, r=1):
    return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])


def Ry(theta, r=1):
    return np.array([[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]])
'''

v01 = np.array([0, 0, 0])
v02 = np.array([2, 8, 0])
A = Graph(1000, 1000, 10, 10, "Pl.svg")
A.bg("black")

A.svg.draw_arrow(v01[0], v01[1], v02[0], v02[1], stroke="white")
A.show()
'''

createDir("Plotsr")
createDir("plotsrast")

frames = 1000
epss = 3.1415 / (180*1.5)
N = 40000

X, Y, Z = lorentz4(4,1,2, N, eps=0.005)

P = np.array([X,Y,Z])

A = Graph(2560, 2560, 30, 30, "s6.svg")
A.bg("black")
A.graph_points(P[0][:], P[1][:], colour="white", strokewidth=1)
A.show()

'''

for i in range(frames):
    A = Graph(1000, 1000, 35, 35, "Plotsr/g" + namer(i) + ".svg", origin=[-10,-2])
    A.bg("black")
    V = np.matmul(Ry(i*epss), P)
    #print(i*epss)
    A.graph_points(V[0][:], V[1][:])
    A.show()
print('l')
create_raster_batch("Plotsr", 'g', 'p', 'plotsrast', frames)
create_mpeg('sav424ee.mp4', 'p', frames, dir=os.getcwd() + "/plotsrast")
'''
'''
def f(t, eps = 0.015, N = 15000):
    def fx(X):
        k = round(eps*t)
        A = np.concatenate([X[0][:k], [None for i in range(len(X)-k-1)]])
        B = np.concatenate([X[1][:k], [None for i in range(len(X)-k-1)]])
        return np.array([A,B])
    return fx
for i in range(frames):
    A = Graph(1000, 1000, 30, 30, "Plotsr/g" + namer(i) + ".svg")
    A.bg("black")
    #print(i*epss)
    V = f(i, eps=N/frames)
    A.graph_points(V(P)[0][:], V(P)[1][:], colour="yellow")
    A.show()
print('l')
create_raster_batch("Plotsr", 'g', 'p', 'plotsrast', frames)
create_mpeg('LiveLorent3.mp4', 'p', frames, dir=os.getcwd() + "/plotsrast")

'''

class Graph3d(Grapher):
    pass